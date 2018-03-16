from django.shortcuts import render
from Schwitter.models import Comment
from Schwitter.models import Post
from Schwitter.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime

# Create your views here.

def viewProfile(request, user):
    context_dict={}
    comments=[]
    posts=Post.objects.filter(poster=user)
    for OP in posts:
        comments.append(Comment.objects.filer(post=OP.post))
    context_dict['posts']=posts
    context_dict['comments']=comments
    response=render(request,'schwitter/user_profile.html',context_dict)
    return response

def viewPost(request, post):
    context_dict={}
    posts=Post.object.filter(post=post)
    comments=Comment.object.filter(post=post.post)
    context_dict['posts']=posts
    context_dict['comments']=comments
    response=render(request,'schwitter/view_post.html',context_dict)
    return response

def register(request):
    registered=False
    if request.method == 'POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered =True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileForm()

    return render(request,'schwitter/register.html',{'user_form':user_form,
                                                     'profile_form':profile_form,
                                                     'registered':registered})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print("Invalid login details: {0},{1}".format(username,password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request,'schwitter/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def add_post(request, user):
    form=post_form()
    if request.method=='POST':
        form=post_form(request.POST)
        if form.is_valid():
            form.poster=user
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request,'schwitter/post.html',{'form':form})

def add_comment(request,user,post):
    form=comment_form()
    if request.method=='POST':
        form=comment_form(request.POST)
        if form.is_valid():
            if post:
                form.poster=user
                form.post=post
                form.save(commit=True)
                return index(request)
        else:
            print(form.errors)
    return render(request,'schwitter/comment.html',{'form':form})
            

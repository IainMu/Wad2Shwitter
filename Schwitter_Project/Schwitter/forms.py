from django import forms
from django.contrib.auth.models import User
from Schwitter.models import UserProfile,Post,Comment

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields = ('username','email','password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('picture',)

class Post_form(forms.ModelForm):
    likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    poster= forms.ModelChoiceField(widget=forms.HiddenInput(),queryset=UserProfile,initial=None)
    time=forms.DateTimeField(widget=forms.HiddenInput(),initial=None)
    class Meta:
        model=Post
        fields = ('title','content',)

class Comment_form(forms.ModelForm):
    likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    post = forms.ModelChoiceField(widget=forms.HiddenInput(),queryset=Post,initial=None)
    poster = forms.ModelChoiceField(widget=forms.HiddenInput(),queryset=UserProfile,initial=None)
    time=forms.DateTimeField(widget=forms.HiddenInput(),initial=None)
    class Meta:
        model=Comment
        fields = ('content',)

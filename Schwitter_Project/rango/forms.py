from django import forms
from django.contrib.auth.models import User
from rango.models import Category, Page, UserProfile

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('picture')

class Post_form(forms.ModelForm):
    class Meta:
        model=Post
        fields(title,content)

class Comment_form(forms.ModelFrom):
    class Meta:
        model=Comment
        fields(content)

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User)
    registered=models.DateTimeField(auto_now_add=True)
    picture=models.ImageField(upload_to='profile_images',blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    poster=models.ForeignKey(UserProfile)
    title=models.TextField(max_length=15)
    time=models.DateTimeField(auto_now_add=True)
    content=models.TextField(max_length=300)
    likes=models.IntegerField(default=0)
    slug=models.SlugField(unique=True)

    def save(self,*args **kwargs):
        self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)

class Comment(models.Model):
    poster=models.ForeignKey(UserProfile)
    post=models.ForeignKey(Post)
    time=models.DateTimeField(auto_now_add=True)
    content=models.TextField(max_length=120)
    likes=models.IntegerField(default=0)
    
    

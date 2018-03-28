from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your models here.

    
class UserProfile(models.Model):
    user=models.OneToOneField(User)
    registered=models.DateTimeField(auto_now_add=True)
    picture=models.ImageField(upload_to='profile_images',default='No_img.jpg')
    #Other users followed by the user
    friends = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    poster=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    title=models.TextField(max_length=15)
    time=models.DateTimeField(auto_now_add=True)
    content=models.TextField(max_length=300)
    likes=models.IntegerField(default=0)
    slug=models.SlugField(unique=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)

class Comment(models.Model):
    poster=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now_add=True)
    content=models.TextField(max_length=120)
    likes=models.IntegerField(default=0)
    
    


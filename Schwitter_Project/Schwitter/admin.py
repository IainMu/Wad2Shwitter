from django.contrib import admin
from Schwitter.models import UserProfile, Post, Comment

# Registered models.
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comment)
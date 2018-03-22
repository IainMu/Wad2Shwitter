from django.conf.urls import url
from Schwitter import views
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

LOGIN_URL = '/Schwitter/login/'
urlpatterns = [
    url(r'^$',views.main, name='home'),
    url(r'profile/(?P<username>[\w\-]+)/$',views.profile,name='profile'),
    url(r'login/$',views.user_login, name='login'),
    url(r'post/$',views.add_post,name='new_post'),
    url(r'profile/(?P<username>[\w\-]+)/(?P<title>[\w\-]+)/$',views.viewPost,name='view_post'),
    url(r'logout/$',views.user_logout,name='logout'),
    url(r'options/$',views.options,name='settings'),
    url(r'register/$',views.register,name='register'),
    url(r'about/$',views.about,name="about"),
    ]

from django import template
from Schwitter.models import Post

register = template.Library()

@register.inclusion_tag('schwitter/home.html' )
def get_post_list():
    #INCOMPLETE
    return {'posts': Post.objects.all()}

@register.inclusion_tag('schwitter/user_profile.html' )
def get_post_list():
    #INCOMPLETE
    #for post in Post.objects.all()
    return {'posts': Post.objects.all()}

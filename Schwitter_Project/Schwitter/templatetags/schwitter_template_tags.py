from django import template
from Schwitter.models import Post,Comment,UserProfile
from django.contrib.auth.models import User
from django.template.loader import get_template

register = template.Library()

#The usual @register.~ wasn't working, found alternative on wiki
y = get_template('schwitter/dash_posts.html')
register.inclusion_tag(y)(get_post_list_dash)
#@register.inclusion_tag('schwitter/dash_posts.html')
def get_post_list_dash(user):
    context_dict={'posts': Post.objects.order_by('time').filter(poster in user.friends)}
    comments=[Comment.objects.order_by('time').filer(Post in Post.objects.filter(poster in user.friends))]
    context_dict['comments'] = comments
    return(context_dict)
    
#@register.inclusion_tag('schwitter/posts.html')
x = get_template('schwitter/posts.html')
register.inclusion_tag(x)(get_post_list_profile)
def get_post_list_profile(poster):
    return{'posts':Post.objects.order_by('time').filter(poster=poster)}

#@register.inclusion_tag('schwitter/comments.html')
z = get_template('schwitter/comments.html')
register.inclusion_tag(z)(get_comment_list)
def get_comment_list(post):
    return{'comments':Comment.objects.order_by('time').filter(post=post)}

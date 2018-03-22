from django import template
from Schwitter.models import Post,Comment,UserProfile
from django.contrib.auth.models import User
from django.template.loader import get_template

register = template.Library()

#The usual @register.~ wasn't working, found alternative on wiki
t = get_template('schwitter/dash_posts.html')
register.inclusion_tag(t)(get_post_list_dash)
def get_post_list_dash(user):
    context_dict={'posts': Post.objects.order_by('time').filter(poster in user.friends)}
    comments=[Comment.objects.order_by('time').filer(Post in Post.objects.filter(poster in user.friends))]
    context_dict['comments'] = comments
    return(context_dict)
    
@register.inclusion_tag('schwitter/posts.html')
def get_post_list_profile(poster):
    return{'posts':Post.objects.order_by('time').filter(poster=poster)}

@register.inclusion_tag('schwitter/comments.html')
def get_comment_list(post):
    return{'comments':Comment.objects.order_by('time').filter(post=post)}

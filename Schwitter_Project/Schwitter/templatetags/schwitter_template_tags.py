from django import template
from schwitter.models import Post,Comment

register = template.Library()

@register.inclusion_tag('schwitter/posts.html')
def get_post_list(poster=None):
    return('posts':Post.objects.filter(poster=poster))

@register.inclusion_tag('schwitter/comments.html')
def get_comment_list(post=None):
    return('comments':Comment.objects.filter(post=post))

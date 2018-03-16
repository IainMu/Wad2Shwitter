from django import template
from Schwitter.models import Post

register = template.Library()

@register.inclusion_tag('schwitter/' )
def get_post_list():
    return {'posts': Post.objects.all()}



from django import template
from ..models import Upvote

register = template.Library()

@register.filter
def is_upvoted_by(tutorial, user):
    upvote = Upvote.objects.filter(user=user, tutorial=tutorial).first()
    return bool(upvote)


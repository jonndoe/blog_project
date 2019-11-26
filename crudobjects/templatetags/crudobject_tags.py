from django import template
from ..models import Crudobject
from django.db.models import Count


register = template.Library()

@register.simple_tag
def total_crudobjects():
    return Crudobject.published.count()


@register.inclusion_tag('crudobjects/latest_crudobjects.html')
def show_latest_crudobjects(count=5):
    latest_crudobjects = Crudobject.published.order_by('-publish')[:count]
    return {'latest_crudobjects': latest_crudobjects}

@register.simple_tag
def get_most_commented_crudobjects(count=5):
    return Crudobject.published.annotate(total_comments=Count('comments')
                                   ).order_by('-total_comments')[:count]
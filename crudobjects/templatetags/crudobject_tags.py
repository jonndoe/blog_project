from django import template

from ..models import Crudobject


register = template.Library()

@register.simple_tag
def total_crudobjects():
    return Crudobject.published.count()


@register.inclusion_tag('crudobjects/latest_crudobjects.html')
def show_latest_crudobjects(count=5):
    latest_crudobjects = Crudobject.published.order_by('-publish')[:count]
    return {'latest_crudobjects': latest_crudobjects}
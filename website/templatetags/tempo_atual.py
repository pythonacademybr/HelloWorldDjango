from django import template
import datetime

register = template.Library()


@register.simple_tag
def tempo_atual():
    return datetime.datetime.now().strftime('%H:%M:%S')

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def primeira_letra(value):
    """
    Verifica se <value> inicia com <arg>.
    :param value: valor do filtro
    :return: True se value iniciar com arg, False caso contrário
    """
    return list(value)[0]

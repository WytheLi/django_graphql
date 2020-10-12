from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='json_script')
def json_script(value, arg):
    return mark_safe('<p id="%s">%s</p>' % (arg, value))
from django import template

register = template.Library()

@register.filter
def append_to_list(value, arg):
    return value + [arg]
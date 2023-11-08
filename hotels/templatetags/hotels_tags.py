from django import template

register = template.Library()

@register.filter
def append_to_list(value, arg):
    return value + [arg]


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def my_set_item(dictionary, key, value):
    dictionary[key] = value
    return ''
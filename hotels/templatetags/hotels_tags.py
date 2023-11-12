# In your views.py
from django import template

register = template.Library()

@register.simple_tag
def set_execution_status(hotel_execution_status, hotel):
    print("Setting execution status")
    hotel_execution_status[hotel] = True
    return ''

@register.filter
def get_execution_status(hotel_execution_status, hotel):
    return hotel_execution_status.get(hotel, False)

register.filter('get_execution_status', get_execution_status)

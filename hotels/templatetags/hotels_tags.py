# In your views.py
from django import template

register = template.Library()

@register.filter
def get_room_reserve_status(is_reserved, room):
    gt=is_reserved.get(room, False)
    return gt

@register.simple_tag
def set_execution_status(hotel_execution_status, hotel):
    hotel_execution_status[hotel] = True
    return ''

@register.filter
def get_execution_status(hotel_execution_status, hotel):
    return hotel_execution_status.get(hotel, False)

register.filter('get_execution_status', get_execution_status)
register.filter('get_room_reserve_status', get_room_reserve_status)

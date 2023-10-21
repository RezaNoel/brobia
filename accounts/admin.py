from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    # list_display = ['hotel_likes','reserves']
    filter_horizontal = ['hotel_likes','reserves']

    def hotel_likes(self, obj):
        hotels = obj.hotels.values_list('faname', flat=True)
        return ", ".join(hotels)
    hotel_likes.short_description = 'هتل های محبوب'
    def reserves(self, obj):
        reserves = obj.requests.values_list('reserve_code', flat=True)
        return ", ".join(requests)
    reserves.short_description = 'رزرو ها'
# Register your models here.
admin.site.register(User,UserAdmin)
from django.contrib import admin
from .models import Hotel, Room,City,Facility,Request
from django.db import models

class HotelAdmin(admin.ModelAdmin):
    list_display = ['name', 'faname', 'address', 'starts', 'city', 'facilities_list', 'slug']
    list_display_links = ['name', 'faname']
    filter_horizontal = ['facilities']

    def facilities_list(self, obj):
        facilities = obj.facilities.values_list('faname', flat=True)
        return ", ".join(facilities)

    facilities_list.short_description = 'امکانات'

class CityAdmin(admin.ModelAdmin):
    list_display = ['name','faname','slug']

class RoomAdmin(admin.ModelAdmin):
    list_display = ['name','faname','price', 'hotel','facilities_list', 'bed','slug','image']
    list_display_links = ['name']
    filter_horizontal = ['facilities']

    def facilities_list(self, obj):
        facilities = obj.facilities.values_list('faname', flat=True)
        return ", ".join(facilities)

    facilities_list.short_description = 'امکانات'


class FacilityAdmin(admin.ModelAdmin):
    list_display = ['name','faname']

class RequestAdmin(admin.ModelAdmin):
    list_display = ['room','enter','exit','room_count','passenger_count']

# ثبت مدل‌ها با استفاده از کلاس‌های Admin
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Request,RequestAdmin)

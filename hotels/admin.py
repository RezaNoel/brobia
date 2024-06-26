from django.contrib import admin
from .models import Hotel, Room, City, Facility, Request, Passenger, HotelImage, Image, RoomImage, ReservasionNumber,Receipt,SeasonPrice
from django.db import models


# Register your models here.


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']


class ImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'file']


class HotelImageInline(admin.TabularInline):
    model = HotelImage


class RoomImageInline(admin.TabularInline):
    model = RoomImage


class HotelAdmin(admin.ModelAdmin):
    list_display = ['faname', 'name', 'address', 'likes', 'stars', 'city', 'facilities_list', 'slug']
    list_display_links = ['name', 'faname']
    filter_horizontal = ['facilities']

    inlines = [HotelImageInline]

    def facilities_list(self, obj):
        facilities = obj.facilities.values_list('faname', flat=True)
        return ", ".join(facilities)

    facilities_list.short_description = 'امکانات'


class CityAdmin(admin.ModelAdmin):
    list_display = ['faname', 'name', 'slug']


class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'faname',  'hotel', 'facilities_list', 'bed', 'slug', 'image']
    list_display_links = ['name']
    filter_horizontal = ['facilities']

    inlines = [RoomImageInline]

    def facilities_list(self, obj):
        facilities = obj.facilities.values_list('faname', flat=True)
        return ", ".join(facilities)

    facilities_list.short_description = 'امکانات'


class FacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'faname', 'related']


class RequestAdmin(admin.ModelAdmin):
    list_display = ['reserve_code', 'get_confirm_status', 'get_reserve_status', 'get_room_name', 'reserve_time']
    search_fields = ['reserve_code', 'room__faname']  # جستجو بر اساس کد رزرو و نام اتاق

    def get_confirm_status(self, obj):
        return obj.get_confirm_display()

    get_confirm_status.short_description = 'وضعیت کانفرم'

    def get_reserve_status(self, obj):
        return obj.get_reserve_status_display()

    get_reserve_status.short_description = 'وضعیت رزرو'

    def get_room_name(self, obj):
        room_name = f'{obj.room.faname} - {obj.room.hotel.faname}'
        return room_name

    get_room_name.short_description = 'اتاق'


class PassengerAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'phone', 'nid', 'birthdate', 'reserves_list']
    list_display_links = ['firstname', 'lastname']
    filter_horizontal = ['reserves']

    def reserves_list(self, obj):
        reserves = obj.reserves.values_list('reserve_code', flat=True)
        return ", ".join(reserves)

    reserves_list.short_description = 'رزرو ها'
class SeasonPriceAdmin(admin.ModelAdmin):
    list_display = ['city','start_date','end_date','season_status']

# ثبت مدل‌ها با استفاده از کلاس‌های Admin
admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Passenger, PassengerAdmin)
admin.site.register(ReservasionNumber)
admin.site.register(SeasonPrice,SeasonPriceAdmin)

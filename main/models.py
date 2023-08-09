from django.db import models
from django.utils.text import slugify
from slugify import slugify as slugify_fa
from django.urls import reverse
from django.db.models import Min

# Create your models here.
import os
def room_image_path_154(instance, filename):
    return os.path.join('static\img','200x154',  filename)
def room_image_path_160(instance, filename):
    return os.path.join('static\img','240x160',  filename)
class City(models.Model):
    name = models.CharField(max_length=75,verbose_name='نام اصلی')
    faname = models.CharField(default="",max_length=75,verbose_name='نام فارسی')
    slug = models.SlugField(default="",null=False,blank=True,db_index=True,verbose_name='لینک')
    def get_absolute_url(self):
        return reverse('hotel-list', args=(self.slug))
    def __str__(self):
        return self.faname
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = ("شهر")
        verbose_name_plural = ("شهر ها")
class Facility(models.Model):
    name = models.CharField(max_length=75,verbose_name='نام اصلی')
    faname = models.CharField(max_length=75,default="",verbose_name='نام فارسی')
    def __str__(self):
        return self.faname
    class Meta:
        verbose_name = ("اماکانات")
        verbose_name_plural = ("امکانات")
class Hotel(models.Model):
    name = models.CharField(max_length=75,verbose_name='نام اصلی')
    faname = models.CharField(default="",max_length=75,verbose_name='نام فارسی')
    address = models.CharField(max_length=75,verbose_name='آدرس')
    starts = models.IntegerField(verbose_name="ستاره")
    city = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name='شهر')
    facilities = models.ManyToManyField(Facility, blank=True,verbose_name='امکانات')
    description = models.TextField(blank=True,verbose_name="توضیحات کوتاه")
    explanation = models.TextField(blank=True,verbose_name="توضیحات بلند")
    slug = models.SlugField(default="",null=False,blank=True,db_index=True,verbose_name='لینک')
    special_offer = models.BooleanField(default=False, verbose_name='آفر ویژه')

    def get_absolute_url(self):
        return reverse('hotel-single', args=(self.slug))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.faname} - {self.city}'

    def min_price(self):
        # کمترین قیمت اتاق‌ها را برای هتل محاسبه کنید و برگردانید
        return Room.objects.filter(hotel=self).aggregate(min_price=Min('price'))['min_price']
    class Meta:
        verbose_name = ("هتل")
        verbose_name_plural = ("هتل ها")
class Room(models.Model):
    name = models.CharField(max_length=75,verbose_name='نام')
    faname = models.CharField(default="",max_length=75,verbose_name='نام نمایشی')
    price = models.IntegerField(verbose_name='قیمت',default=0)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,verbose_name='هتل')
    bed = models.IntegerField(verbose_name='تعداد تخت')
    slug = models.SlugField(default="",null=False,blank=True,db_index=True,verbose_name='لینک')
    image = models.ImageField(blank=True, verbose_name='عکس',upload_to=room_image_path_154)
    image_booking = models.ImageField(blank=True, verbose_name='عکس رزرو',upload_to=room_image_path_160)
    facilities = models.ManyToManyField(Facility, blank=True,verbose_name='امکانات')

    def save(self, *args, **kwargs):
        self.slug = slugify_fa(self.name) + '-' + slugify(self.hotel.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("اتاق")
        verbose_name_plural = ("اتاق ها")
class Request(models.Model):
    room = models.ForeignKey(Room, blank=True,on_delete=models.CASCADE, verbose_name='اتاق')
    enter = models.CharField(max_length=20,verbose_name='ورود')
    exit = models.CharField(max_length=20,verbose_name='خروج')
    room_count = models.IntegerField(verbose_name='تعداد اتاق')
    passenger_count = models.IntegerField(verbose_name='تعداد مسافر')
    confirm = models.BooleanField(default=False, verbose_name='کانفرم')

    class Meta:
        verbose_name = ("درخواست")
        verbose_name_plural = ("درخواست ها")


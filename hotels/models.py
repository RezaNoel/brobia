from django.db import models

# Create your models here.

from django.db import models
from django.utils.text import slugify
from slugify import slugify as slugify_fa
from django.urls import reverse
from django.db.models import Min
import random,string,os
from django.utils import timezone
from datetime import datetime
from jdatetime import datetime as jalali_datetime
# import string

# Create your models here.
def room_image_path_154(instance, filename):
    return os.path.join('static\img','200x154',  filename)
def room_image_path_160(instance, filename):
    return os.path.join('static\img','240x160',  filename)
def room_image_path_550(instance, filename):
    return os.path.join('static\img','820x550',  filename)
class City(models.Model):
    name = models.CharField(max_length=75,verbose_name='نام اصلی')
    faname = models.CharField(default="",max_length=75,verbose_name='نام فارسی')
    slug = models.SlugField(default="",null=False,blank=True,db_index=True,verbose_name='لینک')
    location_distance = models.BooleanField(default=False, verbose_name='دارای مکان محبوب')
    location_name = models.CharField(blank=True,max_length=75, verbose_name='نام مکان محبوب')
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
    RELATED_CHOICES = (
        ('H', 'هتل'),
        ('R', 'اتاق'),
    )

    name = models.CharField(max_length=75,verbose_name='نام آیکون')
    faname = models.CharField(max_length=75,default="",verbose_name='نام فارسی')
    related = models.CharField(max_length=10,choices=RELATED_CHOICES,default="",verbose_name='مربوط')
    def __str__(self):
        return self.faname
    class Meta:
        verbose_name = ("اماکانات")
        verbose_name_plural = ("امکانات")
class Image(models.Model):
    name = models.CharField(blank=True, max_length=100,verbose_name="نام تصویر")
    file = models.ImageField(upload_to=room_image_path_550, verbose_name="فایل تصویر")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = ("تصویر")
        verbose_name_plural = ("تصاویر")
class Hotel(models.Model):
    name = models.CharField(max_length=75,verbose_name='نام اصلی')
    faname = models.CharField(default="",max_length=75,verbose_name='نام فارسی')
    address = models.CharField(max_length=75,verbose_name='آدرس')
    stars = models.IntegerField(verbose_name="ستاره")
    likes = models.IntegerField(default=0 ,verbose_name="لایک ها")
    city = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name='شهر')
    floor = models.IntegerField(default=0 ,verbose_name="تعداد طبقه")
    rooms = models.IntegerField(default=0 ,verbose_name="تعداد اتاق")
    distance = models.FloatField(default=0, verbose_name="فاصله تا مکان محبوب")
    gallery = models.ManyToManyField(Image, through='HotelImage')
    thumbnail = models.ImageField(blank=True, verbose_name='عکس اصلی', upload_to=room_image_path_154)
    facilities = models.ManyToManyField(Facility, blank=True,verbose_name='امکانات')
    description = models.TextField(blank=True,verbose_name="توضیحات کوتاه")
    explanation = models.TextField(blank=True,verbose_name="توضیحات بلند")
    terms = models.TextField(blank=True,verbose_name="قوانین هتل")
    slug = models.SlugField(default="",null=False,blank=True,db_index=True,verbose_name='لینک')
    special_offer = models.BooleanField(default=False, verbose_name='آفر ویژه')
    online_reserve = models.BooleanField(default=False, verbose_name='رزرو آنلاین')
    boroobia_suggest = models.BooleanField(default=False, verbose_name='پیشنهاد بروبیا')

    def increase_likes(self):
        self.likes += 1
        self.save()
    def decrease_likes(self):
        self.likes -= 1
        self.save()

    def get_absolute_url(self):
        return reverse('hotel-single', args=(self.slug))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.faname} - {self.city}'

    def min_price(self):
        # کمترین قیمت اتاق‌ها را برای هتل محاسبه کنید و برگردانید
        min_price = Room.objects.filter(hotel=self).aggregate(min_price=Min('price'))['min_price']

        if min_price is not None:
            # تبدیل عدد به رشته با ویرگول برای جداکردن هر 3 رقم
            formatted_price = '{:,.0f}'.format(min_price)  # اینجا شما می‌توانید تنظیمات نمایش عدد را تغییر دهید
            return formatted_price
        else:
            return "0"  # یا هر پیام دلخواه دیگر برای نمایش در صورت عدم وجود قیمت

    class Meta:
        verbose_name = ("هتل")
        verbose_name_plural = ("هتل ها")

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

class Room(models.Model):
    name = models.CharField(max_length=75,verbose_name='نام')
    faname = models.CharField(default="",max_length=75,verbose_name='نام نمایشی')
    price = models.IntegerField(verbose_name='قیمت',default=0)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,verbose_name='هتل')
    bed = models.IntegerField(verbose_name='تعداد تخت')
    slug = models.SlugField(default="",null=False,blank=True,db_index=True,verbose_name='لینک')
    gallery = models.ManyToManyField(Image, through='RoomImage')
    image = models.ImageField(blank=True, verbose_name='عکس',upload_to=room_image_path_154)
    image_booking = models.ImageField(blank=True, verbose_name='عکس رزرو',upload_to=room_image_path_160)
    facilities = models.ManyToManyField(Facility, blank=True,verbose_name='امکانات')
    is_reserve = models.BooleanField(default=False, verbose_name='خالی / پر')


    def save(self, *args, **kwargs):
        self.slug = slugify_fa(self.name) + '-' + slugify(self.hotel.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.faname+" "+self.hotel.faname

    def format_price(self):
        return '{:,.0f}'.format(self.price)

    class Meta:
        verbose_name = ("اتاق")
        verbose_name_plural = ("اتاق ها")

class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

class ReservasionNumber(models.Model):
    number = models.CharField(max_length=15,verbose_name='شماره رزرواسیون')
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,verbose_name='شماره رزرواسیون')
    class Meta:
        verbose_name = ("شماره رزرواسیون")
        verbose_name_plural = ("شماره رزرواسیون ها")
    def __str__(self):
        return self.number
class Request(models.Model):
    CONFIRM_CHOICES = (
        ('W', 'در انتظار تایید'),
        ('R', 'رد شده'),
        ('A', 'تایید شده'),
    )
    RESERVE_CHOICES = (
        ('WC', 'در انتظار کانفرم'),
        ('WI', 'در انتظار اطلاعات'),
        ('P', 'در انتظار پرداخت'),
        ('R', 'لغو شده'),
        ('D', 'انجام شده'),
    )
    reserve_code = models.CharField(max_length=10, default='xxxxxxxxxx',verbose_name='کد رزرو')
    room = models.ForeignKey(Room, blank=True,on_delete=models.CASCADE, verbose_name='اتاق')
    reservasion_number = models.ForeignKey(ReservasionNumber, default='',on_delete=models.CASCADE,verbose_name='شماره رزرواسیون')
    enter = models.CharField(max_length=15,verbose_name='ورود')
    exit = models.CharField(max_length=20,verbose_name='خروج')
    room_count = models.IntegerField(verbose_name='تعداد اتاق')
    passenger_count = models.IntegerField(verbose_name='تعداد بزرگسال')
    child_count = models.IntegerField(default=0, verbose_name='تعداد خردسال')
    needs = models.CharField(max_length=255, default="",blank=True, verbose_name='نیازمندی ها')
    confirm = models.CharField(max_length=1, choices=CONFIRM_CHOICES, default='W', verbose_name='وضعیت')
    reserve_status = models.CharField(max_length=5, choices=RESERVE_CHOICES, default='WC', verbose_name='وضعیت رزرو')
    reserve_time = models.CharField(default='00:00', max_length=5, verbose_name='زمان رزرو')
    reserve_date = models.DateField(default=timezone.now, verbose_name='تاریخ ثبت رزرو')

    class Meta:
        verbose_name = ("درخواست")
        verbose_name_plural = ("درخواست ها")

    def is_overlapping(self, start_date, end_date):
        return (self.enter < end_date and self.exit > start_date)

    def reserve_date_shamsi(self):
        jalali_date = jalali_datetime.fromgregorian(datetime=self.reserve_date)

        # فرمت دلخواه برای تاریخ جلالی
        formatted_jalali_date = jalali_date.strftime("%Y/%m/%d")

        return formatted_jalali_date
        # jalali_date = JalaliDate(self.reserve_date)
        # return f"{jalali_date.year}/{jalali_date.month:02d}/{jalali_date.day:02d}"

    def reserve_code_save(self):
        code = generate_random_string(10)
        return Room.objects.filter(hotel=self).aggregate(min_price=Min('price'))['min_price']
    def __str__(self):
        return self.reserve_code

class Passenger(models.Model):
    firstname = models.CharField(max_length=75,verbose_name='نام')
    lastname = models.CharField(max_length=75,verbose_name='نام خانوادگی')
    email = models.EmailField(max_length=75,verbose_name='ایمیل',blank=True)
    phone = models.CharField(max_length=11,verbose_name='شماره تماس',blank=True)
    nid = models.CharField(max_length=10,verbose_name='کد ملی')
    birthdate = models.CharField(max_length=15,verbose_name='تاریخ تولد')
    reserves = models.ManyToManyField(Request, blank=True,verbose_name='رزرو ها')

    class Meta:
        verbose_name = ("مسافران")
        verbose_name_plural = ("مسافران")

    def __str__(self):
        return self.firstname+" "+self.lastname

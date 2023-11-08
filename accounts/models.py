from django.db import models
from main.models import Request,Hotel
from django.contrib.auth.models import User,AbstractUser

# Create your models here.
class User(AbstractUser):


    phone = models.CharField(max_length=11, verbose_name='شماره همراه', blank=True)
    nid = models.CharField(max_length=10, blank=True,verbose_name='کد ملی')
    birthdate = models.CharField(max_length=15,blank=True, verbose_name='تاریخ تولد')
    reserves = models.ManyToManyField(Request, blank=True, verbose_name='رزرو ها')
    hotel_likes = models.ManyToManyField(Hotel, blank=True, verbose_name='هتل های محبوب')
    hotel_manager = models.BooleanField(default=False, verbose_name='منیجر هتل')

    def increase_likes(self,hotel):
        if self.hotel_likes.filter(id=hotel.id).exists():
            self.hotel_likes.remove(hotel)
            hotel.likes -= 1
            hotel.save()
        else:
            self.hotel_likes.add(hotel)
            hotel.likes += 1
            hotel.save()
        self.save()

    class Meta:
        verbose_name = ("اطلاعات کاربر")
        verbose_name_plural = ("اطلاعات کاربران")

    def __str__(self):
        return self.get_full_name() or self.username

class HotelManagerModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    class Meta:
        verbose_name = ("اطلاعات منیجر هتل")
        verbose_name_plural = ("اطلاعات منیجر هتل ها")

    def __str__(self):
        return self.get_full_name() or self.username


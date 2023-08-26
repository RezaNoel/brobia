from django.db import models
from main.models import Request
from django.contrib.auth.models import User,AbstractUser

# Create your models here.
class User(AbstractUser):


    phone = models.CharField(max_length=11, verbose_name='شماره همراه', blank=True)
    nid = models.CharField(max_length=10, blank=True,verbose_name='کد ملی')
    birthdate = models.CharField(max_length=15,blank=True, verbose_name='تاریخ تولد')
    reserves = models.ManyToManyField(Request, blank=True, verbose_name='رزرو ها')

    class Meta:
        verbose_name = ("اطلاعات کاربر")
        verbose_name_plural = ("اطلاعات کاربران")

    def __str__(self):
        return self.get_full_name() or self.username





from django.db import models
from main.models import Request
from django.contrib.auth.models import User
# Create your models here.
class ProfileModel(models.Model):
    users = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="کاربر")

    name = models.CharField(max_length=75, verbose_name='نام')
    family = models.CharField(max_length=75, verbose_name='نام خانوادگی')
    phone = models.CharField(max_length=11, verbose_name='شماره تماس', blank=True)
    nid = models.CharField(max_length=10, verbose_name='کد ملی')
    birthdate = models.CharField(max_length=15, verbose_name='تاریخ تولد')
    reserves = models.ManyToManyField(Request, blank=True, verbose_name='رزرو ها')

    class Meta:
        verbose_name = ("اطلاعات کاربر")
        verbose_name_plural = ("اطلاعات کاربران")

    def __str__(self):
        return self.name+" "+self.family





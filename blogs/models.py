from django.db import models

# Create your models here
# functions
def room_image_path_154(instance, filename):
    return os.path.join('static\img','200x154',  filename)
# Models
class BlogCategoryModel(models.Model):
    pass
class BlogModel(models.Model):
    title=models.CharField(max_length=200,verbose_name='تیتر')
    category=models.ForeignKey(BlogCategoryModel,on_delete=models.CASCADE,verbose_name='دسته بندی')
    release_date=models.DateField(auto_now_add=True,verbose_name='تاریخ انتشار')
    description=models.TextField(blank=True ,verbose_name='توضیحات')
    short_description=models.TextField(blank=True, verbose_name='توضیحات کوتاه')
    image=models.ImageField(blank=True,verbose_name='تصاویر',upload_to=room_image_path_154)
    #
    # class Meta:
    #     verbose_name = ("اتاق")
    #     verbose_name_plural = ("اتاق ها")



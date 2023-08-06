# Generated by Django 4.2.3 on 2023-07-25 09:06

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='نام اصلی')),
                ('faname', models.CharField(default='', max_length=75, verbose_name='نام فارسی')),
                ('slug', models.SlugField(blank=True, default='', verbose_name='لینک')),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='نام اصلی')),
                ('faname', models.CharField(default='', max_length=75, verbose_name='نام فارسی')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='نام اصلی')),
                ('faname', models.CharField(default='', max_length=75, verbose_name='نام فارسی')),
                ('address', models.CharField(max_length=75, verbose_name='آدرس')),
                ('starts', models.IntegerField(verbose_name='ستاره')),
                ('description', models.TextField(blank=True, verbose_name='توضیحات کوتاه')),
                ('explanation', models.TextField(blank=True, verbose_name='توضیحات بلند')),
                ('slug', models.SlugField(blank=True, default='', verbose_name='لینک')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.city', verbose_name='شهر')),
                ('facilities', models.ManyToManyField(blank=True, to='main.facility', verbose_name='امکانات')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='نام')),
                ('price', models.IntegerField(default=0, verbose_name='قیمت')),
                ('bed', models.IntegerField(verbose_name='تعداد تخت')),
                ('slug', models.SlugField(blank=True, default='', verbose_name='لینک')),
                ('image', models.ImageField(blank=True, upload_to=main.models.room_image_path_154, verbose_name='عکس')),
                ('image_booking', models.ImageField(blank=True, upload_to=main.models.room_image_path_160, verbose_name='عکس رزرو')),
                ('facilities', models.ManyToManyField(blank=True, to='main.facility', verbose_name='امکانات')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hotel', verbose_name='هتل')),
            ],
        ),
    ]
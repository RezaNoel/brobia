# Generated by Django 4.2.3 on 2023-11-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_city_location_distance_alter_hotel_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='location_name',
            field=models.CharField(blank=True, max_length=75, verbose_name='نام مکان محبوب'),
        ),
    ]
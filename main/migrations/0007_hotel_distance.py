# Generated by Django 4.2.3 on 2023-11-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_hotel_likes_hotel_online_reserve"),
    ]

    operations = [
        migrations.AddField(
            model_name="hotel",
            name="distance",
            field=models.IntegerField(default=0, verbose_name="فاصله تا مکان محبوب"),
        ),
    ]
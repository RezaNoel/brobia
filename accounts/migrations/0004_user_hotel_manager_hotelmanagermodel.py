# Generated by Django 4.2.3 on 2023-11-08 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0014_request_reserve_date"),
        ("accounts", "0003_user_hotel_likes"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="hotel_manager",
            field=models.BooleanField(default=False, verbose_name="منیجر هتل"),
        ),
        migrations.CreateModel(
            name="HotelManagerModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.hotel"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

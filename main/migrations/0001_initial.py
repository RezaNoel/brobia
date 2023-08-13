# Generated by Django 4.2.3 on 2023-08-12 08:28

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("name", models.CharField(max_length=75, verbose_name="نام اصلی")),
                (
                    "faname",
                    models.CharField(
                        default="", max_length=75, verbose_name="نام فارسی"
                    ),
                ),
                ("slug", models.SlugField(blank=True, default="", verbose_name="لینک")),
            ],
            options={
                "verbose_name": "شهر",
                "verbose_name_plural": "شهر ها",
            },
        ),
        migrations.CreateModel(
            name="Facility",
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
                ("name", models.CharField(max_length=75, verbose_name="نام اصلی")),
                (
                    "faname",
                    models.CharField(
                        default="", max_length=75, verbose_name="نام فارسی"
                    ),
                ),
            ],
            options={
                "verbose_name": "اماکانات",
                "verbose_name_plural": "امکانات",
            },
        ),
        migrations.CreateModel(
            name="Hotel",
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
                ("name", models.CharField(max_length=75, verbose_name="نام اصلی")),
                (
                    "faname",
                    models.CharField(
                        default="", max_length=75, verbose_name="نام فارسی"
                    ),
                ),
                ("address", models.CharField(max_length=75, verbose_name="آدرس")),
                ("starts", models.IntegerField(verbose_name="ستاره")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="توضیحات کوتاه"),
                ),
                (
                    "explanation",
                    models.TextField(blank=True, verbose_name="توضیحات بلند"),
                ),
                ("slug", models.SlugField(blank=True, default="", verbose_name="لینک")),
                (
                    "special_offer",
                    models.BooleanField(default=False, verbose_name="آفر ویژه"),
                ),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.city",
                        verbose_name="شهر",
                    ),
                ),
                (
                    "facilities",
                    models.ManyToManyField(
                        blank=True, to="main.facility", verbose_name="امکانات"
                    ),
                ),
            ],
            options={
                "verbose_name": "هتل",
                "verbose_name_plural": "هتل ها",
            },
        ),
        migrations.CreateModel(
            name="Room",
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
                ("name", models.CharField(max_length=75, verbose_name="نام")),
                (
                    "faname",
                    models.CharField(
                        default="", max_length=75, verbose_name="نام نمایشی"
                    ),
                ),
                ("price", models.IntegerField(default=0, verbose_name="قیمت")),
                ("bed", models.IntegerField(verbose_name="تعداد تخت")),
                ("slug", models.SlugField(blank=True, default="", verbose_name="لینک")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        upload_to=main.models.room_image_path_154,
                        verbose_name="عکس",
                    ),
                ),
                (
                    "image_booking",
                    models.ImageField(
                        blank=True,
                        upload_to=main.models.room_image_path_160,
                        verbose_name="عکس رزرو",
                    ),
                ),
                (
                    "facilities",
                    models.ManyToManyField(
                        blank=True, to="main.facility", verbose_name="امکانات"
                    ),
                ),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.hotel",
                        verbose_name="هتل",
                    ),
                ),
            ],
            options={
                "verbose_name": "اتاق",
                "verbose_name_plural": "اتاق ها",
            },
        ),
        migrations.CreateModel(
            name="Request",
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
                    "reserve_code",
                    models.CharField(
                        default="xxxxxxxxxx", max_length=10, verbose_name="کد رزرو"
                    ),
                ),
                ("enter", models.CharField(max_length=20, verbose_name="ورود")),
                ("exit", models.CharField(max_length=20, verbose_name="خروج")),
                ("room_count", models.IntegerField(verbose_name="تعداد اتاق")),
                ("passenger_count", models.IntegerField(verbose_name="تعداد بزرگسال")),
                (
                    "child_count",
                    models.IntegerField(default=0, verbose_name="تعداد خردسال"),
                ),
                (
                    "confirm",
                    models.CharField(
                        choices=[
                            ("W", "در انتظار تایید"),
                            ("R", "رد شده"),
                            ("A", "تایید شده"),
                        ],
                        default="W",
                        max_length=1,
                        verbose_name="وضعیت",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.room",
                        verbose_name="اتاق",
                    ),
                ),
            ],
            options={
                "verbose_name": "درخواست",
                "verbose_name_plural": "درخواست ها",
            },
        ),
    ]

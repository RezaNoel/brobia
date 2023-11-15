# Generated by Django 4.2.3 on 2023-11-15 10:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import hotels.models


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
            options={
                'verbose_name': 'شهر',
                'verbose_name_plural': 'شهر ها',
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='نام آیکون')),
                ('faname', models.CharField(default='', max_length=75, verbose_name='نام فارسی')),
                ('related', models.CharField(choices=[('H', 'هتل'), ('R', 'اتاق')], default='', max_length=10, verbose_name='مربوط')),
            ],
            options={
                'verbose_name': 'اماکانات',
                'verbose_name_plural': 'امکانات',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='نام اصلی')),
                ('faname', models.CharField(default='', max_length=75, verbose_name='نام فارسی')),
                ('address', models.CharField(max_length=75, verbose_name='آدرس')),
                ('stars', models.IntegerField(verbose_name='ستاره')),
                ('likes', models.IntegerField(default=0, verbose_name='لایک ها')),
                ('floor', models.IntegerField(default=0, verbose_name='تعداد طبقه')),
                ('rooms', models.IntegerField(default=0, verbose_name='تعداد اتاق')),
                ('distance', models.IntegerField(default=0, verbose_name='فاصله تا مکان محبوب')),
                ('description', models.TextField(blank=True, verbose_name='توضیحات کوتاه')),
                ('explanation', models.TextField(blank=True, verbose_name='توضیحات بلند')),
                ('terms', models.TextField(blank=True, verbose_name='قوانین هتل')),
                ('slug', models.SlugField(blank=True, default='', verbose_name='لینک')),
                ('special_offer', models.BooleanField(default=False, verbose_name='آفر ویژه')),
                ('online_reserve', models.BooleanField(default=False, verbose_name='رزرو آنلاین')),
                ('boroobia_suggest', models.BooleanField(default=False, verbose_name='پیشنهاد بروبیا')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.city', verbose_name='شهر')),
                ('facilities', models.ManyToManyField(blank=True, to='hotels.facility', verbose_name='امکانات')),
            ],
            options={
                'verbose_name': 'هتل',
                'verbose_name_plural': 'هتل ها',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='نام تصویر')),
                ('file', models.ImageField(upload_to=hotels.models.room_image_path_550, verbose_name='فایل تصویر')),
            ],
            options={
                'verbose_name': 'تصویر',
                'verbose_name_plural': 'تصاویر',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='نام')),
                ('faname', models.CharField(default='', max_length=75, verbose_name='نام نمایشی')),
                ('price', models.IntegerField(default=0, verbose_name='قیمت')),
                ('bed', models.IntegerField(verbose_name='تعداد تخت')),
                ('slug', models.SlugField(blank=True, default='', verbose_name='لینک')),
                ('image', models.ImageField(blank=True, upload_to=hotels.models.room_image_path_154, verbose_name='عکس')),
                ('image_booking', models.ImageField(blank=True, upload_to=hotels.models.room_image_path_160, verbose_name='عکس رزرو')),
                ('facilities', models.ManyToManyField(blank=True, to='hotels.facility', verbose_name='امکانات')),
            ],
            options={
                'verbose_name': 'اتاق',
                'verbose_name_plural': 'اتاق ها',
            },
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.image')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.room')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='gallery',
            field=models.ManyToManyField(through='hotels.RoomImage', to='hotels.image'),
        ),
        migrations.AddField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel', verbose_name='هتل'),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserve_code', models.CharField(default='xxxxxxxxxx', max_length=10, verbose_name='کد رزرو')),
                ('enter', models.CharField(max_length=20, verbose_name='ورود')),
                ('exit', models.CharField(max_length=20, verbose_name='خروج')),
                ('room_count', models.IntegerField(verbose_name='تعداد اتاق')),
                ('passenger_count', models.IntegerField(verbose_name='تعداد بزرگسال')),
                ('child_count', models.IntegerField(default=0, verbose_name='تعداد خردسال')),
                ('needs', models.CharField(blank=True, default='', max_length=255, verbose_name='نیازمندی ها')),
                ('confirm', models.CharField(choices=[('W', 'در انتظار تایید'), ('R', 'رد شده'), ('A', 'تایید شده')], default='W', max_length=1, verbose_name='وضعیت')),
                ('reserve_status', models.CharField(choices=[('WC', 'در انتظار کانفرم'), ('WI', 'در انتظار اطلاعات'), ('P', 'در انتظار پرداخت'), ('R', 'لغو شده'), ('D', 'انجام شده')], default='WC', max_length=5, verbose_name='وضعیت رزرو')),
                ('reserve_time', models.CharField(default='00:00', max_length=5, verbose_name='زمان رزرو')),
                ('reserve_date', models.DateField(default=django.utils.timezone.now, verbose_name='تاریخ ثبت رزرو')),
                ('room', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.room', verbose_name='اتاق')),
            ],
            options={
                'verbose_name': 'درخواست',
                'verbose_name_plural': 'درخواست ها',
            },
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=75, verbose_name='نام')),
                ('lastname', models.CharField(max_length=75, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(blank=True, max_length=75, verbose_name='ایمیل')),
                ('phone', models.CharField(blank=True, max_length=11, verbose_name='شماره تماس')),
                ('nid', models.CharField(max_length=10, verbose_name='کد ملی')),
                ('birthdate', models.CharField(max_length=15, verbose_name='تاریخ تولد')),
                ('reserves', models.ManyToManyField(blank=True, to='hotels.request', verbose_name='رزرو ها')),
            ],
            options={
                'verbose_name': 'مسافران',
                'verbose_name_plural': 'مسافران',
            },
        ),
        migrations.CreateModel(
            name='HotelImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.image')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='gallery',
            field=models.ManyToManyField(through='hotels.HotelImage', to='hotels.image'),
        ),
    ]
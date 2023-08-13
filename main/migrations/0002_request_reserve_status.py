# Generated by Django 4.2.3 on 2023-08-13 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='reserve_status',
            field=models.CharField(choices=[('WC', 'در انتظار کانفرم'), ('WI', 'در انتظار اطلاعات'), ('P', 'در انتظار پرداخت'), ('R', 'لغو شده'), ('D', 'انجام شده')], default='WC', max_length=5, verbose_name='وضعیت رزرو'),
        ),
    ]

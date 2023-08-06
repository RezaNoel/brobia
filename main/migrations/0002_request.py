# Generated by Django 4.2.3 on 2023-07-30 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enter', models.CharField(max_length=20, verbose_name='ورود')),
                ('exit', models.CharField(max_length=20, verbose_name='خروج')),
                ('room_count', models.IntegerField(verbose_name='تعداد اتاق')),
                ('passenger_count', models.IntegerField(verbose_name='تعداد مسافر')),
                ('room', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.room', verbose_name='اتاق')),
            ],
        ),
    ]
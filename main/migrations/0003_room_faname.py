# Generated by Django 4.2.3 on 2023-07-30 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='faname',
            field=models.CharField(default='', max_length=75, verbose_name='نام نمایشی'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_request_confirm'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'شهر', 'verbose_name_plural': 'شهر ها'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'verbose_name': 'اماکانات', 'verbose_name_plural': 'امکانات'},
        ),
        migrations.AlterModelOptions(
            name='hotel',
            options={'verbose_name': 'هتل', 'verbose_name_plural': 'هتل ها'},
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': 'درخواست', 'verbose_name_plural': 'درخواست ها'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'اتاق', 'verbose_name_plural': 'اتاق ها'},
        ),
        migrations.AddField(
            model_name='request',
            name='reserve_code',
            field=models.CharField(default='xxxxxxxxxx', max_length=10),
        ),
    ]
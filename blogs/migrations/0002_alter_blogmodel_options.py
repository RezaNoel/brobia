# Generated by Django 4.2.3 on 2023-11-15 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogmodel',
            options={'verbose_name': 'وبلاگ', 'verbose_name_plural': 'وبلاگ ها'},
        ),
    ]
# Generated by Django 3.2.9 on 2022-03-10 11:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('research', '0002_auto_20220309_2359'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post1',
            new_name='Research',
        ),
    ]
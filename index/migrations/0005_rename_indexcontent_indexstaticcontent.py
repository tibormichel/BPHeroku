# Generated by Django 3.2.9 on 2022-05-18 10:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('index', '0004_rename_indexpost_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IndexContent',
            new_name='IndexStaticContent',
        ),
    ]
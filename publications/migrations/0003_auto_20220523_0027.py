# Generated by Django 3.2.9 on 2022-05-22 22:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_auto_20220517_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='body',
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]

# Generated by Django 3.2.9 on 2022-05-24 23:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0002_auto_20220517_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='body',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='research',
            name='body_sk',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
# Generated by Django 3.2.9 on 2022-05-24 23:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_post_tmp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tmp',
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='body_sk',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]

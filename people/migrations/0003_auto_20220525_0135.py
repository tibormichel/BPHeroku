# Generated by Django 3.2.9 on 2022-05-24 23:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_person_maisid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='body',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='body_sk',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]

# Generated by Django 3.2.9 on 2022-05-24 23:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_pategory_title_sk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='body',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='body_sk',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]

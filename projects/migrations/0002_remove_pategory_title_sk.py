# Generated by Django 3.2.9 on 2022-05-17 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pategory',
            name='title_sk',
        ),
    ]

# Generated by Django 3.2.9 on 2022-05-17 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0009_auto_20220516_0828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='research',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='research',
            name='related_project',
        ),
        migrations.RemoveField(
            model_name='research',
            name='related_publication',
        ),
    ]

# Generated by Django 3.2.9 on 2022-03-09 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post1',
            old_name='author1',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post1',
            old_name='body1',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='post1',
            old_name='title1',
            new_name='title',
        ),
    ]
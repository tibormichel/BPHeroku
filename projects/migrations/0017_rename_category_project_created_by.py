# Generated by Django 3.2.9 on 2022-04-30 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_rename_created_by_project_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='category',
            new_name='created_by',
        ),
    ]

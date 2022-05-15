# Generated by Django 3.2.9 on 2022-05-01 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0031_alter_project_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ManyToManyField(related_name='projects', to='projects.Category'),
        ),
    ]

# Generated by Django 3.2.9 on 2022-03-17 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20220317_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(default='uncategorized', max_length=255),
        ),
    ]
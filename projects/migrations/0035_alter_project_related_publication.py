# Generated by Django 3.2.9 on 2022-05-01 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0010_auto_20220501_0223'),
        ('projects', '0034_auto_20220501_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='related_publication',
            field=models.ManyToManyField(to='publications.Publication'),
        ),
    ]
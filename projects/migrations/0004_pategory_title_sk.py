# Generated by Django 3.2.9 on 2022-05-22 09:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20220517_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='pategory',
            name='title_sk',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
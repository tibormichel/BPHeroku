# Generated by Django 3.2.9 on 2022-05-18 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='maisID',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
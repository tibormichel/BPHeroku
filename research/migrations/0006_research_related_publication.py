# Generated by Django 3.2.9 on 2022-05-01 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0010_auto_20220501_0223'),
        ('research', '0005_alter_research_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='related_publication',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='publications.publication'),
        ),
    ]

# Generated by Django 3.2.9 on 2022-05-16 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0008_auto_20220514_2117'),
        ('publications', '0011_auto_20220512_1126'),
        ('projects', '0040_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='related_publication',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='publications.publication'),
        ),
        migrations.AlterField(
            model_name='project',
            name='related_research',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='research.research'),
        ),
    ]

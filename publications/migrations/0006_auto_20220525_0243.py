# Generated by Django 3.2.9 on 2022-05-25 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20220525_0135'),
        ('people', '0004_auto_20220525_0208'),
        ('research', '0003_auto_20220525_0137'),
        ('publications', '0005_auto_20220525_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='created_by',
            field=models.ManyToManyField(blank=True, null=True, to='people.Person'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='related_project',
            field=models.ManyToManyField(blank=True, null=True, to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='related_research',
            field=models.ManyToManyField(blank=True, null=True, to='research.Research'),
        ),
    ]

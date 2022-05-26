# Generated by Django 3.2.9 on 2022-05-25 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20220525_0208'),
        ('projects', '0006_auto_20220525_0135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='related_publication',
        ),
        migrations.RemoveField(
            model_name='project',
            name='related_research',
        ),
        migrations.RemoveField(
            model_name='project',
            name='created_by',
        ),
        migrations.AddField(
            model_name='project',
            name='created_by',
            field=models.ManyToManyField(blank=True, null=True, to='people.Person'),
        ),
    ]
# Generated by Django 3.2.9 on 2022-04-30 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_alter_person_status'),
        ('index', '0006_remove_post_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='test',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='people.person'),
        ),
    ]
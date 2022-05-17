# Generated by Django 3.2.9 on 2022-04-30 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_alter_person_status'),
        ('index', '0003_remove_post_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='test',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='people.person'),
            preserve_default=False,
        ),
    ]
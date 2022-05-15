# Generated by Django 3.2.9 on 2022-04-30 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_alter_person_status'),
        ('research', '0004_research_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='people.person'),
        ),
    ]

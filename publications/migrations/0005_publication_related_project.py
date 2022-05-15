# Generated by Django 3.2.9 on 2022-05-01 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0028_auto_20220501_0211'),
        ('publications', '0004_publication_related_research'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='related_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
    ]
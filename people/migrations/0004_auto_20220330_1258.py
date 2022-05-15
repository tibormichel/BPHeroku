# Generated by Django 3.2.9 on 2022-03-30 10:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_doctorand_employee_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='author',
        ),
        migrations.RemoveField(
            model_name='student',
            name='author',
        ),
        migrations.AddField(
            model_name='person',
            name='status',
            field=models.CharField(choices=[('Emplyee', 'Employee'), ('Student', 'Student'), ('Doctorand', 'Doctorand')], default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Doctorand',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]

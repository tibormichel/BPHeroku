import requests
from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Person(models.Model):
    title = models.CharField(max_length=255)
    title_sk = models.CharField(max_length=255, blank=True, null=True)
    maisID = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=256, choices=[('Employee', 'Employee'), ('Student', 'Student'), ('Doctorand', 'Doctorand'), ('Uncategorized', 'Uncategorized') ])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null = True, blank=True)
    body = RichTextField(blank=True, null = True)
    body_sk = RichTextField(blank=True, null=True)
    # timetable = requests.get("https://kpi:GWsy6BfLfc9rUB03tT6e@maisutils.tuke.sk/export/?vystup=rozvrh_pedagoga&login=" + ).json()


    def __str__(self):
        return self.title


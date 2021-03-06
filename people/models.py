import requests
from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Person(models.Model):
    title = models.CharField(max_length=255)
    maisID = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=256, choices=[('Employee', 'Employee'), ('Student', 'Student'), ('Doctorand', 'Doctorand'), ('Uncategorized', 'Uncategorized') ])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True, default='../static/profilePic.png')
    body = RichTextField(null = True)
    body_sk = RichTextField(null=True)

    def __str__(self):
        return self.title


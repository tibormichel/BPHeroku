from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    title = models.CharField(max_length=255)
    title_sk = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(null=True)
    body_sk = RichTextField(null=True)
    link = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


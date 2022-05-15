from django.db import models
from django.contrib.auth.models import User
from people.models import Person
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_sk = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True)
    body_sk = RichTextField(blank=True, null=True)
    def __str__(self):
        return self.title + ' | ' + str(self.author)
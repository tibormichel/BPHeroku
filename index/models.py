from django.db import models
from django.contrib.auth.models import User
from people.models import Person
from ckeditor.fields import RichTextField

class IndexStaticContent(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.ImageField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    text_sk = models.TextField(null=True, blank=True)
    def __str__(self):
        return "indexstaticContent"

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_sk = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(null=True)
    body_sk = RichTextField(null=True)


    def __str__(self):
        return self.title
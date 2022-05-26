from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User

from people.models import Person



class Research(models.Model):
    title = models.CharField(max_length=255)
    title_sk = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_by = models.ManyToManyField(Person, blank=True)
    body = RichTextField(null=True)
    body_sk = RichTextField(null=True)

    def __str__(self):
        return self.title
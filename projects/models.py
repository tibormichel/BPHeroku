from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from people.models import Person


class Pategory(models.Model):
    title = models.CharField(max_length=255)
    # title_sk = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255)
    title_sk = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Pategory, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(Person, on_delete=models.CASCADE, default=1)
    related_publication = models.ForeignKey('publications.Publication', on_delete=models.CASCADE, null=True, blank=True)
    related_research = models.ForeignKey('research.Research', on_delete=models.CASCADE, null=True, blank=True)
    body = RichTextField(blank=True)
    body_sk = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

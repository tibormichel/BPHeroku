from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from people.models import Person
# from projects.models import Project
# from publications.models import Publication

class Research(models.Model):
    title = models.CharField(max_length=255)
    title_sk = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Person, on_delete=models.CASCADE, default=1)
    related_publication = models.OneToOneField('publications.Publication', on_delete=models.CASCADE, null=True, blank=True)
    related_project = models.OneToOneField('projects.Project', on_delete=models.CASCADE, null=True, blank=True)
    body = RichTextField(blank=True)
    body_sk = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
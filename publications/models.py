from django.db import models
from django.contrib.auth.models import User
from people.models import Person
from projects.models import Project
from research.models import Research



class Publication(models.Model):
    title = models.CharField(max_length=255, null=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_by = models.ManyToManyField(Person,blank=True)

    related_project = models.ManyToManyField(Project,blank=True)
    related_research = models.ManyToManyField(Research,blank=True)


    def __str__(self):
        return self.title
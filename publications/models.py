from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from people.models import Person
from projects.models import Project
#
from research.models import Research



class Publication(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # created_by = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True) #toto bolo namiesto riadku pod tym
    created_by = models.ManyToManyField(Person)
    related_project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    related_research = models.ForeignKey(Research, on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.title #+ ' | ' + str(self.author)
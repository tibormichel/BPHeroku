from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User
from people.models import Person


class Category(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    title_sk = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    # category_name = category.title

    # created_by = models.ForeignKey(Person, on_delete=models.CASCADE, default=1, null=True, blank=True) totot
    # related_publication = models.OneToOneField('publications.Publication', on_delete=models.CASCADE, null=True)
    # related_publication = models.ManyToManyField('publications.Publication', related_name='publication')
    # related_publication = models.ManyToManyRel('publications.Publication', related_name='publication')
    # related_publication = models.ManyToManyField('publications.Publication')
    # related_publication = models.ForeignKey('publications.Publication', on_delete=models.CASCADE, null=True, blank=True)ttttt
    # related_research = models.ForeignKey('research.Research', on_delete=models.CASCADE, null=True, blank=True)tttttt
    # related_research = models.OneToOneField('research.Research', on_delete=models.CASCADE, null=True)
    body = RichTextField(blank=True, null=True)
    body_sk = RichTextField(blank=True, null=True)
    # def __str__(self):
    #     template = self.title + ' | ' + str(self.author)
    #     return template.format(self)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

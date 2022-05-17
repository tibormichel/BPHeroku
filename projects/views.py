from django.views.generic import ListView, DetailView

# Create your views here.
from django.shortcuts import render, HttpResponse

from .models import Project, Pategory


# Create your views here.

from django.shortcuts import render, HttpResponse

# def projects(request):
# #   return HttpResponse("Hello world!")
#     return render(request, "projects/projects.html", dict())

class HomeView(ListView,):
    model = Project
    template_name = 'projects/projects.html'

def CategoryListView(request, cats):
    category_projects = Project.objects.filter(category__title = cats)
    return render(request, 'projects/categories_list.html', {'cats':cats, 'category_projects':category_projects})

class CategoriesView(ListView):
    model = Pategory
    template_name = 'projects/categories.html'

class ArticleDetailView(DetailView):
    model = Project
    template_name = 'projects/project_details.html'
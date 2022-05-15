
from django.views.generic import ListView, DetailView


from .models import Person

class HomeView(ListView):

    model = Person
    template_name = 'people/people.html'

class ArticleDetailView(DetailView):
    model = Person
    template_name = 'people/person_details.html'


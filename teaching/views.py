from django.views.generic import ListView
from .models import Subject

class HomeView(ListView):
    model = Subject
    template_name = 'teaching/teaching.html'

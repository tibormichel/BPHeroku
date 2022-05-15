from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
from django.shortcuts import render, HttpResponse

from research.models import Research
# def research(request):
# #   return HttpResponse("Hello world!")
#
#
#     return render(request, "research/research.html", {"name": "test"})

class HomeView(ListView):
    model = Research
    template_name = 'research/research.html'

class ArticleDetailView(DetailView):
    model = Research
    template_name = 'research/research_details.html'


from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, DetailView

# Create your views here.
from django.shortcuts import render, HttpResponse

from index.models import Post


# def index(request):
# #   return HttpResponse("Hello world!")
#     return render(request, "index/index.html", dict())

class HomeView(ListView):
    model = Post
    # title = _(model.title)
    # body = _(model.body)

    template_name = 'index/index.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'index/article_details.html'
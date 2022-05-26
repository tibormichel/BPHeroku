from django.views.generic import ListView, DetailView

from .filters import PublicationFilter
from .models import Publication

class HomeView(ListView):
    model = Publication
    template_name = 'publications/publications.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PublicationFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ArticleDetailView(DetailView):
    model = Publication
    template_name = 'publications/publication_details.html'
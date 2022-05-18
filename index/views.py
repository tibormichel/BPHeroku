from django.views import View
from django.views.generic import ListView, DetailView
from index.models import Post, IndexStaticContent


class HomeView(ListView):
    model = Post
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['more_model_objects'] = IndexStaticContent.objects.first()
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'index/article_details.html'


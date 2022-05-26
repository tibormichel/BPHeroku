from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView

urlpatterns = [

    path('',HomeView.as_view(), name="publications"),
    path('publication/<int:pk>', ArticleDetailView.as_view(), name='publication-detail'),
]
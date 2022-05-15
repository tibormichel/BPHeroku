from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView


urlpatterns = [
   # path("", views.index, name="index"), #1 verzia bez adminpanelu
    path('',HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
]

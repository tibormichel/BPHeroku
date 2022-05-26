from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, CategoriesView, CategoryListView

urlpatterns = [

    path('',HomeView.as_view(), name="projects"),
    path('categories', CategoriesView.as_view(), name='project-category'),

    path('category/<str:cats>', CategoryListView, name='category-detail'),
    path('project/<int:pk>', ArticleDetailView.as_view(), name='project-detail'),
]
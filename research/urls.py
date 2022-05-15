from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView

urlpatterns = [
    #path("", views.research, name="research"),
    path('',HomeView.as_view(), name="research"),
    path('research/<int:pk>', ArticleDetailView.as_view(), name='research-detail'),
]
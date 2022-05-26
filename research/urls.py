from django.urls import path

from .views import HomeView, ArticleDetailView

urlpatterns = [

    path('',HomeView.as_view(), name="research"),
    path('research/<int:pk>', ArticleDetailView.as_view(), name='research-detail'),
]
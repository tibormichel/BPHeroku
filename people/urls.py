from django.urls import path

from .views import HomeView, ArticleDetailView



urlpatterns = [
    path('',HomeView.as_view(), name="people"),


    path('person/<int:pk>', ArticleDetailView.as_view(), name='person-detail'),

]
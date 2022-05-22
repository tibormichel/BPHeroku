from django.urls import path

from . import views
from .views import HomeView, ArticleDetailView



urlpatterns = [
    path('',HomeView.as_view(), name="people"),


    path('person/<int:pk>', ArticleDetailView.as_view(), name='person-detail'),
    # path('person/<int:pk>', views.home, name='home'),
]
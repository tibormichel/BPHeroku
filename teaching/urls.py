from django.urls import path
from . import views

urlpatterns = [
    path("", views.teaching, name="teaching"),
]
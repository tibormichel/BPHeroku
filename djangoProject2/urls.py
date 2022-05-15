"""djangoProject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import  i18n_patterns
from django.views.static import serve

urlpatterns = [

    path('admin/', admin.site.urls),
    ]

urlpatterns += i18n_patterns(

    path("calculator_app/",include("calculator.urls")),

    path('',include("index.urls")),
    path("research/", include("research.urls")),
    path("people/", include("people.urls")),
    path("projects/", include("projects.urls")),
    path("publications/", include("publications.urls")),
    path("teaching/", include("teaching.urls")),
    path("contact/", include("contact.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

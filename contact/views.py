
# Create your views here.

from django.shortcuts import render, HttpResponse

def contact(request):
#   return HttpResponse("Hello world!")
    return render(request, "contact/contact.html", dict())
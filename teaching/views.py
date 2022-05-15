
# Create your views here.

from django.shortcuts import render, HttpResponse

def teaching(request):
#   return HttpResponse("Hello world!")
    return render(request, "teaching/teaching.html", dict())
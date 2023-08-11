from django.http import HttpResponse
from django.shortcuts import render
from .models import Advertisement

def index(request):
    advertisements =  Advertisement.objects.all()
    context ={'advertisements': advertisements}
    return render( request, "index.html", context)

def lessonFour(request):
    return HttpResponse("Урок номер 4")

def top_sellers(requests):
    return render (requests, 'top-sellers.html')


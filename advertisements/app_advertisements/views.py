from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render( request, "index.html")

def lessonFour(request):
    return HttpResponse("Урок номер 4")

def top_sellers(requests):
    return render (requests, 'top-sellers.html')


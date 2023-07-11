from django.http import HttpResponse
from django.shortcuts import render

def index(reqest):
    return render( reqest, "index.html")

def lessonFour(reqest):
    return HttpResponse("Урок номер 4")

def top_sellers(reqests):
    return render (reqests, 'top-sellers.html')


from django.urls import path
from .views import index, lessonFour, top_sellers

urlpatterns = [
    path('', index),
    path('lesson_4/', lessonFour),
    path('top-sellers/', top_sellers),
]


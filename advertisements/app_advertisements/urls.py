from django.urls import path
from .views import index, lessonFour, top_sellers

urlpatterns = [
    path('', index, name = 'main-page'),
    path('lesson_4/', lessonFour),
    path('top-sellers/', top_sellers, name = 'top-sellers'),
]


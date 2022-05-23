from django.contrib import admin
from django.urls import path, include

from practiceapp.views import practice_first, create_code

app_name = 'practiceapp'

urlpatterns = [
    path('', practice_first, name='firstpractice'),
    path('create/', create_code, name='create'),
]
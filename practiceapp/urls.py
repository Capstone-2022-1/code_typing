from django.contrib import admin
from django.urls import path, include

from practiceapp.views import practice_first

app_name = 'practiceapp'

urlpatterns = [
    path('', practice_first, name='firstpractice'),
]
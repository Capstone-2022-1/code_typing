from django.contrib import admin
from django.urls import path, include

from practiceapp.views import practice_first, practice_create, practice_second, practice_result

app_name = 'practiceapp'

urlpatterns = [
    path('', practice_first, name='firstpractice'),
    path('create/', practice_create, name='create'),
    path('second/', practice_second, name='second'),
    path('result/', practice_result, name='result'),

]
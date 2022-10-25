from django.contrib import admin
from django.urls import path, include

from practiceapp.views import practice_first, practice_create, practice_second, result, manage_result

app_name = 'practiceapp'

urlpatterns = [
    path('', practice_first, name='firstpractice'),
    path('create/', practice_create, name='create'),
    path('second/', practice_second, name='second'),
    path('second/result', result, name='result'),
    path('manage/', manage_result, name='manage'),

]
from django.contrib import admin
from django.urls import path, include

from upracticeapp.views import upractice_first

app_name = 'upracticeapp'

urlpatterns = [
    path('', upractice_first, name='ufirstpractice'),
]
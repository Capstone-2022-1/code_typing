from django.contrib import admin
from django.urls import path, include

from mainapp.views import main_page

app_name = 'mainapp'

urlpatterns = [
    path('', main_page, name='mainpage'),
]
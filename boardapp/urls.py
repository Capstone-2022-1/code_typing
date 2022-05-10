from django.contrib import admin
from django.urls import path, include

from boardapp.views import main_board

app_name = 'boardapp'

urlpatterns = [
    path('', main_board, name='mainboard'),
]
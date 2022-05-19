from django.contrib import admin
from django.urls import path, include

from gameapp.views import first_game

app_name = 'gameapp'

urlpatterns = [
    path('', first_game, name='playgame'),
]
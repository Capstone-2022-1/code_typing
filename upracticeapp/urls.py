from django.contrib import admin
from django.urls import path, include

from upracticeapp.views import upractice_main, upractice_first, upractice_second

app_name = 'upracticeapp'

urlpatterns = [
    path('', upractice_main, name='mainupractice'),
    path('ucreate/', upractice_first, name='ufirstpractice'),
    path('second/<int:upractice_id>', upractice_second, name='usecondpractice'),
]
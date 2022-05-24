from django.contrib import admin
from django.urls import path, include

from upracticeapp.views import upractice_first, upractice_main, upractice_second

app_name = 'upracticeapp'

urlpatterns = [
    path('', upractice_main, name='mainupractice'),
    path('ucreate/', upractice_first, name='ufirstpractice'),
    path('second/', upractice_second, name='usecondpractice'),
]
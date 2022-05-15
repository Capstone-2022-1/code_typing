from django.contrib import admin
from django.urls import path, include

from boardapp.views import main_board

app_name = 'boardapp'

urlpatterns = [
    path('mainboard/', main_board, name='mainboard'),
    # path('list/', BoardListView.as_view(), name='list'),
    # path('create/', BoardCreateView.as_view(), name='create'),
    # path('detail/<int:pk>/', BoardDetailView.as_view(), name='detail'),
]
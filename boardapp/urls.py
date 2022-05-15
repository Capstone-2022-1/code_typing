from django.contrib import admin
from django.urls import path, include

from boardapp.views import CategoryListView, CategoryCreateView, CategoryDetailView

app_name = 'boardapp'

urlpatterns = [
    path('list/', CategoryListView.as_view(), name='list'),
    path('create/', CategoryCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', CategoryDetailView.as_view(), name='detail'),
]
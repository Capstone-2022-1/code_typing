from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from postapp.views import PostCreateView, PostDetailView

app_name = 'postapp'

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='postapp/list.html'), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),

]

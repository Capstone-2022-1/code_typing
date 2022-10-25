from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from mainapp.views import main_page, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView, \
    practice_result

app_name = 'mainapp'

urlpatterns = [
    path('', main_page, name='mainpage'),
    path('signup/', AccountCreateView.as_view(), name='signup'),

    path('login/', LoginView.as_view(template_name='mainapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
    path('practice_result/<int:pk>', practice_result, name='practice_result'),
]
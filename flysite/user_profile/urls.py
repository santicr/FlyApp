from .views import login, register, profile
from django.urls import path

urlpatterns = [
    path('login/', login, name = 'login'),
    path('register/', register, name = 'register'),
    path('', profile, name = 'profile')
]
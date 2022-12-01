from .views import login_req, register, profile, logout_req
from django.urls import path

urlpatterns = [
    path('login/', login_req, name = 'login'),
    path('logout/', logout_req, name = 'logout'),
    path('register/', register, name = 'register'),
    path('', profile, name = 'profile')
]
from .views import add_ticket
from django.urls import path

urlpatterns = [
    path('add_ticket/<int:flight_id>', add_ticket, name = 'add_ticket'),
]
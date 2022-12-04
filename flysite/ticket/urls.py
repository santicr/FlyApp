from .views import add_ticket, pay_ticket
from django.urls import path

urlpatterns = [
    path('add_ticket/<int:flight_id>', add_ticket, name = 'add_ticket'),
    path('pay_ticket/<int:ticket_id>', pay_ticket, name = 'pay_ticket'),
]
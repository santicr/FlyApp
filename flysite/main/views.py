from django.shortcuts import render
from django.contrib.auth.models import User
from flight.models import Flight
from ticket.models import Ticket
from datetime import datetime, timedelta

# Create your views here.
def index(req):
    tickets_to_delete = {}
    time_now = datetime.now()

    for ticket in Ticket.objects.all():
        created = ticket.created + timedelta(days = 1)
        day, hour, minute = created.day, created.hour, created.minute
        
        if time_now.day == day and time_now.hour == hour and time_now.minute == minute and not ticket.paid:
            tickets_to_delete[ticket.id] = 1

    for k in tickets_to_delete:
        ticket = Ticket.objects.get(id = k)
        ticket.delete()

    flights = Flight.objects.all()
    return render(req, 'main/index.html', {'flights': flights})
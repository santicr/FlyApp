from django.shortcuts import render
from django.contrib.auth.models import User
from flight.models import Flight
from ticket.models import Ticket
from datetime import datetime, timedelta, date
from .forms import FilterForm

# Create your views here.
def index(req):
    form = FilterForm()
    flights = None
    tickets_to_delete = {}

    for ticket in Ticket.objects.all():
        year = int(ticket.created.year)
        day = int(ticket.created.day)
        month = int(ticket.created.month)
        today = datetime.now()
        year_today = int(today.year)
        day_today = int(today.day)
        month_today = int(today.month)
        cond1 = date(year, month, day) + timedelta(days = 1) <= date(year_today, month_today, day_today) and not ticket.paid
        cond2 = ticket.flight.quantity
        if (cond1) or (cond2 <= 0):
            tickets_to_delete[ticket.id] = 1

    for k in tickets_to_delete:
        ticket = Ticket.objects.get(id = k)
        print(ticket)
        ticket.delete()

    if req.method == 'POST':
        data = req.POST
        form = FilterForm(data)

        if form.is_valid():
            source = data['source']
            destination = data['destination']
            number_of_connections = int(data['number_of_connections'])
            flights = Flight.objects.filter(source = source).filter(destination = destination).filter(number_of_connections = number_of_connections).filter(quantity__gte = 1)
    elif req.method == 'GET':
        flights = Flight.objects.all().filter(quantity__gte = 1)

    return render(req, 'main/index.html', {'flights': flights, 'form': form})
from django.shortcuts import render
from django.contrib.auth.models import User
from flight.models import Flight
from ticket.models import Ticket
from datetime import datetime, timedelta
from .forms import FilterForm

# Create your views here.
def index(req):
    form = FilterForm()
    flights = Flight.objects.all()

    if req.method == 'POST':
        data = req.POST
        form = FilterForm(data)
        if form.is_valid():
            source = data['source']
            destination = data['destination']
            number_of_connections = int(data['number_of_connections'])
            flights = Flight.objects.filter(source = source).filter(destination = destination).filter(number_of_connections = number_of_connections)

    return render(req, 'main/index.html', {'flights': flights, 'form': form})
from django.shortcuts import render
from django.contrib.auth.models import User
from flight.models import Flight

# Create your views here.
def index(req):
    flights = Flight.objects.all()
    return render(req, 'main/index.html', {'flights': flights})
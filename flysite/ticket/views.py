from django.shortcuts import render, redirect
from .models import Ticket

# Create your views here.
def add_ticket(req, flight_id):
    if req.user.is_authenticated:
        return redirect('profile')
    return redirect('index')

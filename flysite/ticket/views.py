from django.shortcuts import render, redirect, HttpResponse
from .models import Ticket
from flight.models import Flight
from .forms import TicketForm
from threading import Lock

# Create your views here.
def add_ticket(req, flight_id):
    if req.user.is_authenticated:
        form = TicketForm()

        if req.method == 'POST':
            data = req.POST
            form = TicketForm(data)

            if form.is_valid():
                name = data['name']
                lastname1 = data['lastname1']
                lastname2 = data['lastname2']
                cc = data['cc']
                user_profile = req.user
                flight_id = flight_id
                ticket = Ticket(name=name, lastname1=lastname1, lastname2=lastname2, cc=cc, user_profile=user_profile, flight_id=flight_id)
                ticket.save()
                return redirect('index')

        return render(req, 'ticket/ticket.html', {'form': form, 'flight_id': flight_id})
    return redirect('login')

def pay_ticket(req, ticket_id):
    lock = Lock()
    lock.acquire()

    ticket = Ticket.objects.get(id = ticket_id)
    if ticket.flight.quantity <= 0:
        ticket.delete()
        return HttpResponse('Lo siento, ya se han comprado estos boletos justo antes de tu compra')
    else:
        ticket.flight.quantity -= 1
        ticket.paid = True
        ticket.flight.save()
        ticket.save()
        
    lock.release()
    return redirect('profile')
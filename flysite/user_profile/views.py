from django.shortcuts import render, redirect
from .forms import NewUserCreationForm, NewAuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages as m
from ticket.models import Ticket
from flight.models import Flight
from datetime import datetime, date

# Create your views here.
def login_req(req):
    if not req.user.is_authenticated:
        form = NewAuthenticationForm()
        if req.method == 'POST':
            data = req.POST
            form = NewAuthenticationForm(req, data = data)

            if form.is_valid():
                username = data['username']
                password = data['password']
                user_profile = authenticate(username = username, password = password)

                if user_profile is not None:
                    login(req, user_profile)
                    m.success(req, 'Has iniciado correctamente!')
            else:
                m.error(req, 'Datos incorrectos, intenta de nuevo!')
            
            return redirect('index')
        return render(req, 'user_profile/login.html', {'login': 1, 'form': form})
    return redirect('index')

def logout_req(req):
    if req.user.is_authenticated:
        logout(req)
        m.success(req, 'Has cerrado sesión exitosamente!')
    return redirect('index')

def register(req):
    form = NewUserCreationForm()
    if not req.user.is_authenticated:
        
        if req.method == 'POST':
            data = req.POST
            print(data)
            form = NewUserCreationForm(data)
            if form.is_valid():
                form.save()
                m.info(req, 'Te has registrado correctamente!')
            else:
                m.error(req, 'No cumpliste los requerimientos de contraseña o usuario, intenta de nuevo!')

            return redirect('index')
        return render(req, 'user_profile/register.html', {'register': 1, 'form': form})
    return redirect('index')

def comp_lt(ticket: Ticket):
    time = ticket.flight.departure_time
    ticket_time_compare = (date(int(time.year), int(time.month), int(time.day)))
    time_now = datetime.now()
    time_compare = date(int(time_now.year), int(time_now.month), int(time_now.day))
    return ticket_time_compare < time_compare

def comp_gte(ticket: Ticket):
    time = ticket.flight.departure_time
    ticket_time_compare = (date(int(time.year), int(time.month), int(time.day)))
    time_now = datetime.now()
    time_compare = date(int(time_now.year), int(time_now.month), int(time_now.day))
    return ticket_time_compare >= time_compare

def profile(req):
    if req.user.is_authenticated:
        old_tickets = list(filter(comp_lt, Ticket.objects.filter(user_profile = req.user)))
        pending_tickets = Ticket.objects.filter(user_profile = req.user).filter(paid = False)
        paid_tickets = list(filter(comp_gte, Ticket.objects.filter(user_profile = req.user).filter(paid = True)))
        return render(req, 'user_profile/profile.html',{
            'pending_tickets': pending_tickets, 'paid_tickets': paid_tickets, 'old_tickets': old_tickets
        })
    return redirect('index')
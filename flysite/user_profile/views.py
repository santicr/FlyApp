from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages as m

# Create your views here.
def login_req(req):
    form = AuthenticationForm()
    if not req.user.is_authenticated:
        if req.method == 'POST':
            form = AuthenticationForm(req, req.POST)

            if form.is_valid():
                username = form.cleaned_data.get('username')
                passw = form.cleaned_data.get('password')
                user_profile = authenticate(username = username, password = passw)

                if user_profile is not None:
                    login(req, user_profile)
                    m.success(req, 'Has iniciado sesión correctamente!')
                    return redirect('index')

        return render(req, 'user_profile/login.html', {'login': 1, 'form': form})
    return redirect('index')

def logout_req(req):
    if req.user.is_authenticated:
        logout(req)
        m.info(req, 'Has cerrado sesión exitosamente!')
    return redirect('index')

def register(req):
    form = UserCreationForm()
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            m.success(req, 'Te has registrado correctamente!')
        else:
            m.error(req, "Hubo un error, intenta de nuevo!")
        return redirect('index')

    return render(req, 'user_profile/register.html', {'register': 1, 'form': form})

def profile(req):
    return render(req, 'user_profile/profile.html')
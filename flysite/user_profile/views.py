from django.shortcuts import render

# Create your views here.
def login(req):
    return render(req, 'user_profile/login.html', {'login': 1})

def register(req):
    return render(req, 'user_profile/register.html', {'register': 1})

def profile(req):
    return render(req, 'user_profile/profile.html')
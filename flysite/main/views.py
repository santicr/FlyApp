from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(req):
    return render(req, 'main/index.html')
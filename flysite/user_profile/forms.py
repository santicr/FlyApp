from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class NewUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario', required=True, widget = forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    password1 = forms.CharField(label='Contraseña', required=True, widget = forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))
    password2 = forms.CharField(label='Confirma la contraseña', required=True, widget = forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))

class NewAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario', required=True, widget= forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    password = forms.CharField(label='Contraseña', required=True, widget = forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))
from django import forms

class TicketForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, widget = forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    lastname1 = forms.CharField(max_length=30, required=True, widget = forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    lastname2 = forms.CharField(max_length=30, required=True, widget = forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    cc = forms.CharField(max_length=20, required=True, widget = forms.TextInput(
        attrs={'class': 'form-control'}
    ))
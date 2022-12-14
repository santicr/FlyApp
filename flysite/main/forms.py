from django import forms
from flight.models import City

class FilterForm(forms.Form):
    cities = list(City.objects.all())
    city_choices = [(city.name, city.name) for city in cities]
    connections_choices = [(i, i) for i in range(5)]

    source = forms.ChoiceField(
        choices = city_choices,
        label='Ciudad de origen'
    )

    destination = forms.ChoiceField(
        choices = city_choices,
        label = 'Ciudad de destino'
    )

    number_of_connections = forms.ChoiceField(
        choices = connections_choices,
        label = 'Numero de conexiones'
    )
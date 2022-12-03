from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'Ciudad: {self.name}'

class Flight(models.Model):
    airline = models.CharField(max_length=150)
    source = models.CharField(max_length=100)
    connections = models.ManyToManyField(City, null=True, blank=True)
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    number_of_connections = models.IntegerField(default=0)
    destination = models.CharField(max_length=100)
    cost = models.FloatField()

    def __str__(self):
        return f'Vuelo #{self.id} desde {self.source} con {self.number_of_connections} conexiones'
from django.db import models
from flight.models import Flight
from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
    name = models.CharField(max_length=30)
    lastname1 = models.CharField(max_length=30)
    lastname2 = models.CharField(max_length=30)
    cc = models.CharField(max_length=20)
    flight = models.OneToOneField(Flight, on_delete=models.PROTECT)
    user_profile = models.ForeignKey(User, on_delete=models.PROTECT)
    paid = models.BooleanField()
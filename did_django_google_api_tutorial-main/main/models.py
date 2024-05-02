from django.db import models

# Create your models here.
class Vehicle(models.Model):
    registration_number = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
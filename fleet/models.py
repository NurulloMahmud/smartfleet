from django.db import models
from hiring.models import Driver
from management.models import Company



class TruckMake(models.Model):
    name = models.CharField(max_length=50)


class TruckModel(models.Model):
    name = models.CharField(max_length=50)


class Truck(models.Model):
    unit_number = models.CharField(max_length=20)
    year = models.IntegerField()
    make = models.ForeignKey(TruckMake, on_delete=models.CASCADE)
    model = models.ForeignKey(TruckModel, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    carrier = models.ForeignKey(Company, on_delete=models.CASCADE)
    
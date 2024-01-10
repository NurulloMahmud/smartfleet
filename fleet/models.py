from django.db import models
from management.models import Company



class TruckMake(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TruckModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Truck(models.Model):
    unit_number = models.CharField(max_length=20)
    year = models.IntegerField()
    make = models.ForeignKey(TruckMake, on_delete=models.CASCADE)
    model = models.ForeignKey(TruckModel, on_delete=models.CASCADE)
    driver = models.ForeignKey('hiring.Driver', on_delete=models.CASCADE, 
                               null=True, blank=True, related_name='assigned_trucks')
    carrier = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.unit_number
        
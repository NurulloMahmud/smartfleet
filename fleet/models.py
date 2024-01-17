from django.db import models
from management.models import Company



class TruckStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


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
    vin = models.CharField(max_length=17)
    year = models.IntegerField()
    make = models.ForeignKey(TruckMake, on_delete=models.CASCADE)
    model = models.ForeignKey(TruckModel, on_delete=models.CASCADE)
    carrier = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.unit_number


class TruckInUse(models.Model):
    drivers = models.ManyToManyField('hiring.Driver')
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    pick_up = models.DateField(null=True, blank=True)
    drop = models.DateField(null=True, blank=True)
    start_milage = models.IntegerField(null=True, blank=True)
    end_milage = models.IntegerField(null=True, blank=True)
    fuel_level = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.drivers.__str__() + str(self.truck.unit_number)
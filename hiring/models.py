from django.db import models
from management.models import Company



class Status(models.Model):
    name = models.CharField(max_length=50)
    deleted = models.BooleanField(default=False)
    last_update = models.DateField(auto_now=True)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()
    
    def __str__(self) -> str:
        return self.name


class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    cdl = models.IntegerField(unique=True, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    truck = models.ForeignKey('fleet.Truck', on_delete=models.CASCADE, 
                              null=True, blank=True, related_name='assigned_driver')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    last_update = models.DateField(auto_now=True)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()
    
    def __str__(self):
        return self.first_name

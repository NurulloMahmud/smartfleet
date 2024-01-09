from django.db import models




class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    cdl = models.IntegerField(unique=True, null=True, blank=True)

    
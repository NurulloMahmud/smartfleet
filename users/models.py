from django.db import models
from django.contrib.auth.models import AbstractUser



class Department(models.Model):
    name = models.CharField(max_length=50)


class User(AbstractUser):
    phone_number = models.CharField(max_length=15)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    authorized = models.BooleanField(default=False)


from django.db import models
from django.contrib.auth.models import AbstractUser


class UserStatus(models.Model):
    name = models.CharField(max_length=50)


class Department(models.Model):
    name = models.CharField(max_length=50)


class User(AbstractUser):
    phone_number = models.CharField(max_length=15)
    status = models.ForeignKey(UserStatus, on_delete=models.CASCADE)
    password = models.TextField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    verification_link = models.TextField(null=True, blank=True)

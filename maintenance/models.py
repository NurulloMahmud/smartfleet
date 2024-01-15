from django.db import models



class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Case(models.Model):
    case_number = models.CharField(max_length=50, null=True, blank=True)
    truck = models.ForeignKey('fleet.Truck', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    shop_address = models.TextField(null=True, blank=True)
    shop_name = models.CharField(max_length=500, null=True, blank=True)
    shop_number = models.CharField(max_length=50, null=True, blank=True)
    shop_in = models.DateTimeField(null=True, blank=True)
    shop_out = models.DateTimeField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    days_in_shop = models.IntegerField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    expense = models.CharField(max_length=500)

    def __str__(self) -> str:
        return str(self.truck.unit_number)


class Note(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    staff = models.ForeignKey('users.User', on_delete=models.CASCADE)
    note = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return str(self.case.truck.unit_number)


class Odometer(models.Model):
    truck = models.ForeignKey('fleet.Truck', on_delete=models.CASCADE)
    ododmeter = models.FloatField()
    date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.truck.unit_number} >>> {self.date}"
    

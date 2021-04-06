from django.db import models
from datetime import date



class Expense(models.Model):
    month = models.CharField(max_length=9)
    category = models.CharField(max_length=64)
    allocated = models.DecimalField(max_digits=8, decimal_places=2)
    disbursed = models.DecimalField(max_digits=8, decimal_places=2)
    remaining = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.category} {self.month}'

class Transaction(models.Model):
    date =models.DateField(default=date.today)
    recipient = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    inflow = models.DecimalField(max_digits=8, decimal_places=2)
    outflow = models.DecimalField(max_digits=8, decimal_places=2)
    note = models.TextField()

    def __str__(self):
        return f'{self.recipient} {self.category} {self.note}'

from django.db import models
from datetime import date



class Expense(models.Model):
    month = models.CharField(max_length=9)
    category = models.CharField(max_length=64)
    allocated = models.DecminalField(max_digits=8, decimal_places=2)
    spent = models.DecminalField(max_digits=8, decimal_places=2)
    remaining = models.DecminalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return '%s %s' % (self.month, self.category)

class Transaction(models.Model):
    date =models.DateField(default=date.today)
    payee = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    inflow = models.DecminalField(max_digits=8, decimal_places=2)
    outflow = models.DecimalField(max_digits=8, decimal_places=2)
    note = models.TextField()

    def __str__(self):
        return '%s %s %s' % (self.payee, self.category, self.note)

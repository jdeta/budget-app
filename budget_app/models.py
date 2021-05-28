from django.db import models
from datetime import date


class Category(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
      return self.name

class Expense(models.Model):
    month = models.DateField(default=date.today)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    allocated = models.DecimalField(max_digits=8, decimal_places=2)
    disbursed = models.DecimalField(max_digits=8, decimal_places=2)
    remaining = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        get_latest_by = 'month'

    def __str__(self):
        return f'{self.category} {self.month}'

class Transaction(models.Model):
    date = models.DateField(default=date.today)
    recipient = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    inflow = models.DecimalField(max_digits=8, decimal_places=2)
    outflow = models.DecimalField(max_digits=8, decimal_places=2)
    note = models.TextField()

    def __str__(self):
        return f'{self.recipient} {self.category} {self.note}'


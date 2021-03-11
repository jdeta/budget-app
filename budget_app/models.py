from django.db import models

class Expense(models.Model):
    amount = models.DecimalField(max_digits=6,decimal_places=2)
    exp_type = models.CharField(max_length=50)
    exp_date = models.DateTimeField('date purchased')

    def __str__(self):
        return self.exp_type

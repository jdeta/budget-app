from django.db import models
from datetime import date



class ExpenseInfo(models.Model):
    date = models.DateField(default=date.today)
    cost = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        abstract = True


class PayPeriod(models.Model):
    start_date = models.DateField()
    end_date=models.DateField()
    paycheck = models.DecimalField(max_digits=8, decimal_places=2)


class FixedExpense(ExpenseInfo):
    exp_type = models.CharField(max_length=24)
    pay_period = models.ForeignKey(PayPeriod, on_delete=models.CASCADE)

    def __str__(self):
        return self.exp_type


class Envelopes(models.Model):
    env_name = models.CharField(max_length=24)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    pay_period = models.ForeignKey(PayPeriod, on_delete=models.CASCADE)

    def __str__(self):
        return self.env_name


class NonFixedExpense(ExpenseInfo):
    envelope = models.ForeignKey(Envelopes, on_delete=models.CASCADE)
    note = models.TextField()

    def __str__(self):
        return self.note

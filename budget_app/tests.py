from django.test import TestCase
from datetime import date

from .models import PayPeriod

class PayPeriodModelTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        #sample data for running tests
        PayPeriod.objects.create(start_date='2021-04-01',end_date='2021-04-14',paycheck=2000.00)

    def test_start_date_label(self):
        period = PayPeriod.objects.get(pk=1)
        start_label = period._meta.get_field('start_date').verbose_name
        self.assertEqual(start_label, 'start date')

    def test_end_date_label(self):
        period = PayPeriod.objects.get(pk=1)
        end_label = period._meta.get_field('end_date').verbose_name
        self.assertEqual(end_label, 'end date')

    def test_paycheck_label(self):
        period = PayPeriod.objects.get(pk=1)
        pay_label = period._meta.get_field('paycheck').verbose_name
        self.assertEqual(pay_label, 'paycheck')

    def test_paycheck_max_digits(self):
         period = PayPeriod.objects.get(pk=1)
         digits = period._meta.get_field('paycheck').max_digits
         self.assertEqual(digits, 8)

    def test_start_isbefore_end(self):
        period = PayPeriod.objects.get(pk=1)
        self.assertIs(period.end_date > period.start_date, True)

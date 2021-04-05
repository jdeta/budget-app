from django.test import TestCase
from datetime import date

from .models import Expense, Transaction

class ExpenseModelTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        #sample data for running tests
        Expense.objects.create(month ='Apr 2021', category='mortgage', allocated=600, spent=0, remaining=600)

    def test_month_label(self):
        expense_item = Expense.objects.get(pk=1)
        month_label = expense_item._meta.get_field('month').verbose_name
        self.assertEqual(month_label, 'month')

    def test_category_label(self):
        expense_item = Expense.objects.get(pk=1)
        category_label = expense_item._meta.get_field('category').verbose_name
        self.assertEqual(category_label, 'category')

    def test_allocated_label(self):
        expense_item = Expense.objects.get(pk=1)
        allocated_label = expense_item._meta.get_field('allocated').verbose_name
        self.assertEqual(allocated_label, 'allocated')

    def test_spent_label(self):
        expense_item = Expense.objects.get(pk=1)
        spent_label = expense_item._meta.get_field('spent').verbose_name
        self.assertEqual(spent_label, 'spent')

    def test_remaining_label(self):
        expense_item = Expense.objects.get(pk=1)
        remaining_label = expense_item._meta.get_field('remaining').verbose_name
        self.assertEqual(remaining_label, 'remaining')

    def test_allocated_max_digits(self):
         expense_item = Expense.objects.get(pk=1)
         allocated_digits = expense_item._meta.get_field('allocated').max_digits
         self.assertEqual(allocated_digits, 8)

    def test_spent_max_digits(self):
         expense_item = Expense.objects.get(pk=1)
         spent_digits = expense_item._meta.get_field('spent').max_digits
         self.assertEqual(spent_digits, 8)

    def test_remaining_max_digits(self):
         expense_item = Expense.objects.get(pk=1)
         remaining_digits = expense_item._meta.get_field('remaining').max_digits
         self.assertEqual(remaining_digits, 8)

    def test_month_max_length(self):
        expense_item = Expense.objects.get(pk=1)
        month_length = expense_item._meta.get_field('month').max_length
        self.assertEqual(month_length, 9)

    def test_category_max_length(self):
        expense_item = Expense.ojbects.get(pk=1)
        category_length = expense_item._meta.get_field('category'.max_length
        self.assertEqual(category_length, 64)

    def test_month_str_output(self):
        expense_item = Expense.object.get(pk=1)
        self.assertEqual(expense_item.month, str(expense_item.month))

    def test_category_string_output(self):
        expense_item = Expense.object.get(pk=1)
        self.assertEqual(expense_item.category, str(expense_item.category)

class TransactionModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        #sample data for running tests
        Transaction.objects.create(date='2021-04-01', category='paycheck', payee='me', inflow=2000, outflow=0, note='bi-weekly paycheck')

    def test_date_label(self):
        fake_transaction = Transaction.objects.get(pk=1)
        date_label = expense_item._meta.get_field('date').verbose_name
        self.assertEqual(date_label, 'date')

    def test_payee_label(self):
        fake_transaction = Transaction.objects.get(pk=1)
        payee_label = expense_item._meta.get_field('payee').verbose_name
        self.assertEqual(payee_label, 'payee')

    def test_category_label(self):
        fake_transaction = Transaction.objects.get(pk=1)
        category_label = expense_item._meta.get_field('category').verbose_name
        self.assertEqual(category_label, 'category')

    def test_inflow_label(self):
        fake_transaction = Transaction.objects.get(pk=1)
        inflow_label = expense_item._meta.get_field('inflow').verbose_name
        self.assertEqual(inflow_label, 'inflow')

    def test_outflow_label(self):
        fake_transaction = Transaction.objects.get(pk=1)
        outflow_label = expense_item._meta.get_field('outflow').verbose_name
        self.assertEqual(outflow_label, 'outflow')
  
      def test_note_label(self):
        fake_transaction = Transaction.objects.get(pk=1)
        note_label = expense_item._meta.get_field('note').verbose_name
        self.assertEqual(note_label, 'note')

    def test_inflow_max_digits(self):
         fake_transaction = Transaction.objects.get(pk=1)
         inflow_digits = expense_item._meta.get_field('inflow').max_digits
         self.assertEqual(inflow_digits, 8)

    def test_outflow_max_digits(self):
         fake_transaction = Transaction.objects.get(pk=1)
         outflow_digits = expense_item._meta.get_field('outflow').max_digits
         self.assertEqual(outflow_digits, 8)

    def test_payee_max_length(self):
        fake_transaction = Transaction.objects.get(pk=1)
        payee_length = expense_item._meta.get_field('payee').max_length
        self.assertEqual(month_length, 9)

    def test_category_max_length(self):
        fake_transaction = Transaction.objects.get(pk=1)
        category_length = expense_item._meta.get_field('category'.max_length
        self.assertEqual(category_length, 64)

    def test_payee_str_output(self):
        fake_transaction = Transaction.objects.get(pk=1)
        self.assertEqual(fake_transaction.payee, str(fake_transaction.payee))

    def test_category_string_output(self):
        fake_transaction = Transaction.objects.get(pk=1)
        self.assertEqual(fake_transaction.category, str(fake_transaction.category)

      def test_note_string_output(self):
        fake_transaction = Transaction.objects.get(pk=1)
        self.assertEqual(fake_transaction.note, str(fake_transaction.note)

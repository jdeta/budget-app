from django.core.exceptions import ObjectDoesNotExist
from .models import Expense
from datetime import date, datetime

def update_expense(new_transaction):
    if Expense.objects.filter(category=new_transaction.category).exists():
        expense_to_update = Expense.objects.get(category=new_transaction.category)
        expense_to_update.disbursed = expense_to_update.disbursed - new_transaction.outflow
        expense_to_update.remaining = expense_to_update.allocated + expense_to_update.disbursed
        expense_to_update.save()
    else:
        pass


def latest_months_expenses():
    latest_expense = Expense.objects.filter(month__isnull=False).latest()
    latest_date = str(latest_expense.month)
    stripped_date = datetime.strptime(latest_date, "%Y-%m-%d")

    all_current_expenses = Expense.objects.filter(month__month=stripped_date.month)
    return all_current_expenses

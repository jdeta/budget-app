from django.core.exceptions import ObjectDoesNotExist
from .models import Expense
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

def update_expense(new_transaction):
    if Expense.objects.filter(category=new_transaction.category).exists():
        expense_to_update = Expense.objects.get(category=new_transaction.category)
        expense_to_update.disbursed = expense_to_update.disbursed - new_transaction.outflow
        expense_to_update.remaining = expense_to_update.allocated + expense_to_update.disbursed
        expense_to_update.save()
    else:
        pass



def latest_month():
    latest_expense = Expense.objects.filter(month__isnull=False).latest()
    month_string = str(latest_expense.month)
    strpd_date = datetime.strptime(month_string, "%Y-%m-%d")
    return strpd_date

def latest_months_expenses():
    current_month = latest_month()
    current_expenses = Expense.objects.filter(month__month=current_month.month)
    return current_expenses

def new_month():
    to_copy = latest_months_expenses()
    old_expense_list = []
    new_expense_list = []

    for expense in to_copy:
        old_expense_list.append(expense)
    
    for item in old_expense_list:
        new_expense_list.append(Expense(
                month=item.month+relativedelta(months=+1),
                category=item.category,
                allocated=0.00,
                disbursed=0.00,
                remaining=0.00))

    Expense.objects.bulk_create(new_expense_list)



from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense, Transaction
from .forms import NewTransactionForm, NewExpenseForm
from datetime import date, timedelta


def budget_dashboard(request):
    expenses = Expense.objects.all()
    return render(request, 'budget_app/dashboard.html', {'expenses':expenses})


def new_transaction(request):
    if request.method == 'POST':
        transaction_form = NewTransactionForm(request.POST)

        if transaction_form.is_valid():
            transaction_form.save()
            return redirect('/')

    else:
        transaction_form = NewTransactionForm()
        return render(request, 'budget_app/transaction_new.html', {'transaction_form': transaction_form})


def new_expense(request):
    if request.method == 'POST':
        expense_form = NewExpenseForm(request.POST)

        if expense_form.is_valid():
            expense_added = expense_form.save(commit=False)
            expense_added.allocated = 0.00
            expense_added.disbursed = 0.00
            expense_added.remaining = 0.00
            expense_added.month = 'Apr 2021'
            expense_added.save()
            return redirect('/')

    else:
        expense_form = NewExpenseForm()
        return render(request, 'budget_app/expense_new.html', {'expense_form': expense_form})

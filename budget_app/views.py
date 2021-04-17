from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Expense, Transaction
from .forms import NewTransactionForm, NewExpenseForm, UpdateAllocationForm
from datetime import date, timedelta


def budget_dashboard(request):
    expenses = Expense.objects.all()
    total_transactions = Transaction.objects.all().aggregate(Sum('inflow'))['inflow__sum'] or 0.00
    total_allocations = expenses.aggregate(Sum('allocated'))['allocated__sum'] or 0.00
    unbudgeted = total_transactions - total_allocations
    context = {
            'expenses':expenses,
            'unbudgeted':unbudgeted,
    }

    return render(request, 'budget_app/dashboard.html', context)


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


def expense_detail(request, expense_id):
    specific_expense = get_object_or_404(Expense, pk=expense_id)

    if request.method == 'POST':
        allocated_form = UpdateAllocationForm(request.POST, instance=specific_expense)

        if allocated_form.is_valid():
            allocated_form.save()
            return redirect('/')
    else:
        allocated_form = UpdateAllocationForm(instance=specific_expense)
        return render(request, 'budget_app/expense_detail.html', {'specific_expense':specific_expense, 'allocated_form':allocated_form})

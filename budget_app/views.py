from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Expense, Transaction
from .forms import NewTransactionForm, NewExpenseForm, UpdateAllocationForm, NewCategoryForm
from datetime import date, timedelta
from decimal import Decimal as dc


def budget_dashboard(request):
    expenses = Expense.objects.all()
    total_transactions = Transaction.objects.all().aggregate(Sum('inflow'))['inflow__sum'] or dc(0.00)
    total_allocations = expenses.aggregate(Sum('allocated'))['allocated__sum'] or dc(0.00)
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
        category_form = NewCategoryForm()
        context = {
            'transaction_form': transaction_form,
            'category_form': category_form
            }
        return render(request, 'budget_app/transaction_new.html', context)


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
        category_form = NewCategoryForm()
        expense_form = NewExpenseForm()
        return render(request, 'budget_app/expense_new.html', {'expense_form': expense_form, 'category_form':category_form})


def expense_detail(request, expense_id):
    specific_expense = get_object_or_404(Expense, pk=expense_id)

    if request.method == 'POST':
        allocated_form = UpdateAllocationForm(request.POST)

        if allocated_form.is_valid():
            specific_expense.allocated = specific_expense.allocated + allocated_form.cleaned_data['allocate']
            specific_expense.remaining = specific_expense.allocated - specific_expense.disbursed
            specific_expense.save()
            return redirect('/')
    else:
        allocated_form = UpdateAllocationForm()
        return render(request, 'budget_app/expense_detail.html', {'specific_expense':specific_expense, 'allocated_form':allocated_form})

def new_category_transaction(request):
    if request.method == 'POST':
        category_form = NewCategoryForm(request.POST)

        if category_form.is_valid():
            category_form.save()
            return redirect('budget_app:new_transaction')

    else:
        category_form = NewCategoryForm()
        return render(request, 'budget_app/category_new.html', {'category_form':category_form})

def new_category_expense(request):
    if request.method == 'POST':
        category_form = NewCategoryForm(request.POST)

        if category_form.is_valid():
            category_form.save()
            return redirect('budget_app:new_expense')

    else:
        category_form = NewCategoryForm()
        return render(request, 'budget_app/category_new.html', {'category_form':category_form})

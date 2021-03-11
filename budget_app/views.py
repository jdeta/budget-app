from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm


def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'budget_app/expense_list.html', {'expenses': expenses})

def expense_new(request):
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            expense = form.save()
            return redirect('budget_app:expense_list')

    else:
        form = ExpenseForm()
    return render(request, 'budget_app/expense_add.html', {'form': form})

def expense_del(request, pk):
    goner = get_object_or_404(Expense, pk=pk)
    context = {}

    if request.method == "POST":
        goner.delete()
        return redirect('budget_app:expense_list')

    return render(request, 'budget_app/expense_list.html', context)

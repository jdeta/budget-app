from django import forms
from .models import Expense, Transaction

class NewExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ('category',)

class UpdateAllocationForm(forms.Form):
    allocate = forms.DecimalField(max_digits=8, decimal_places=2)

class NewTransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ('date', 'recipient', 'category', 'inflow', 'outflow', 'note')

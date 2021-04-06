from django import forms
from .models import Expense, Transaction

class NewExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ('category',)


class NewTransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ('date', 'recipient', 'category', 'inflow', 'outflow', 'note')

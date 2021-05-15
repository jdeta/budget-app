from .models import Expense

def update_expense(new_transaction):
    if Expense.objects.filter(category=new_transaction.category).exists():
        expense_to_update = Expense.objects.get(category=new_transaction.category)
        expense_to_update.disbursed = expense_to_update.disbursed - new_transaction.outflow
        expense_to_update.remaining = expense_to_update.allocated + expense_to_update.disbursed
        expense_to_update.save()
    else:
        pass

from django.contrib import admin
from .models import Expense, Transaction, Category

admin.site.register(Expense)
admin.site.register(Transaction)
admin.site.register(Category)

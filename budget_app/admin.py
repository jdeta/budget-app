from django.contrib import admin
from .models import Expense, Transaction

admin.site.register(Expense)
admin.site.register(Transaction)

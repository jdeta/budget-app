from django.contrib import admin
from .models import PayPeriod, FixedExpense, Envelopes, NonFixedExpense

admin.site.register(PayPeriod)
admin.site.register(FixedExpense)
admin.site.register(Envelopes)
admin.site.register(NonFixedExpense)


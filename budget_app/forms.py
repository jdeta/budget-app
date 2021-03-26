from django import forms
from .models import PayPeriod

class PayPeriodForm(forms.ModelForm):

    class Meta:
        model = PayPeriod
        fields = ('start_date', 'end_date', 'paycheck')

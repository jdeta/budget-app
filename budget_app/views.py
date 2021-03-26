from django.shortcuts import render, redirect, get_object_or_404
from .models import PayPeriod, FixedExpense, Envelopes, NonFixedExpense
from .forms import PayPeriodForm

def budget_dashboard(request):
    current_period = PayPeriod.objects.latest('start_date')
    context = {
            'current_period':current_period
            }

    return render(request, 'budget_app/dashboard.html', context)


def new_pay_period(request):
    if request.method == 'POST':
        pp_form = PayPeriodForm(request.POST)

        if form.is_valid():
            pp_added = pp_form.save()
            
            return redirect('budget_app:dashboard')

        else:
            pp_form = PayPeriodForm()

        return render(request, 'budget_app/new_pp.html', {'pp_form': pp_form})


#def expense_del(request, pk):
#    goner = get_object_or_404(Expense, pk=pk)
#    context = {}

 #   if request.method == "POST":
 #       goner.delete()
 #       return redirect('budget_app:expense_list')

  #  return render(request, 'budget_app/expense_list.html', context)

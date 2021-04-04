from django.shortcuts import render, redirect, get_object_or_404
from .models import PayPeriod, FixedExpense, Envelopes, NonFixedExpense
from .forms import PayPeriodForm
from datetime import date, timedelta

def budget_dashboard(request):
    current_period = PayPeriod.objects.latest('start_date')
    context = {
            'current_period':current_period
            }

    return render(request, 'budget_app/dashboard.html', context)


def new_pay_period(request):
    if request.method == 'POST':
        pp_form = PayPeriodForm(request.POST)

        if pp_form.is_valid():
            pp_added = pp_form.save(commit=False)
            pp_added.end_date = pp_added.start_date + timedelta(days=13)
            pp_added.save()
            return redirect('/')

    else:
        pp_form = PayPeriodForm()
        return render(request, 'budget_app/new_pp.html', {'pp_form': pp_form})


def new_envelope(request, payperiod_id):
    if request.method == 'POST':
        env_form = EnvelopeForm(request.POST)

        if env_form.is_valid():
            env_added = evn_form.save(commit=False)
            current_period = PayPeriod.objects.latest('start_date')
            env_added.pay_period = current_period
            env_added.save()
            return redirect('/')

    else:
        env_form =EnvelopeForm()
        return render(request, 'budget_app/new_env.html', {'env_form': env_form}

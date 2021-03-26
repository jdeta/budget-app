from django.urls import path
from . import views


app_name = 'budget_app'
urlpatterns = [
    path('', views.budget_dashboard, name='budget_dashboard'),
    path('payperiod/new', views.new_pay_period, name='new_pay_period'),
]

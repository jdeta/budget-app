from django.urls import path
from . import views


app_name = 'budget_app'
urlpatterns = [
    path('', views.budget_dashboard, name='budget_dashboard'),
    path('expense/new', views.new_expense, name='new_expense'),
    path('transaction/new', views.new_transaction, name='new_transaction'),
]

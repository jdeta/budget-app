from django.urls import path
from . import views


app_name = 'budget_app'
urlpatterns = [
    path('', views.budget_dashboard, name='budget_dashboard'),
    path('expense/new', views.new_expense, name='new_expense'),
    path('expense/<int:expense_id>/' ,views.expense_detail, name='expense_detail'),
    path('transaction', views.transaction_detail, name='transaction_detail'),
    path('expense/delete/<int:expense_id>/',views.del_expense, name='del_expense'),
    path('transaction/new', views.new_transaction, name='new_transaction'),
    path('expense/category/new', views.new_category_expense, name = 'new_category_expense'),
    path('transaction/category/new', views.new_category_transaction, name='new_category_transaction'),
    path('month_new', views.add_next_month, name = 'add_next_month')
    
]

from django.urls import path
from . import views


app_name = 'budget_app'
urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('expense/new', views.expense_new, name='expense_new'),
    path('expense/<int:pk>/del',  views.expense_del, name='expense_del'),
]

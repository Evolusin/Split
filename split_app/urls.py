from django.urls import path
from . import views

app_name = 'split_app'
urlpatterns = [
    path('',views.index, name='index'),
    path('transactions/', views.transactions, name ='Transactions'),
    path('transactions/<int:transaction_id>/', views.transaction, name='transaction'),
    path('new_transaction/', views.new_transaction, name='new_transaction'),
    path('new_obligation/<int:transaction_id>/', views.new_obligation, name='new_obligation'),
    path('edit_obligation/<int:obligation_id>/', views.edit_obligation, name='edit_obligation'),
]
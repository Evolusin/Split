from django.urls import path
from . import views

app_name = 'split_app'
urlpatterns = [
    path('',views.index, name='index'),
    path('transactions/', views.transactions, name ='Transactions'),
    path('transactions/<int:transaction_id>/', views.transaction, name='transaction')
]
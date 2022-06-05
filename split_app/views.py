from django.shortcuts import render
from .models import Transaction, Obligation

# Create your views here.
def index(req):
    return render(req,'split_app/index.html')

def transactions(req):
    "Show all transactions"
    transactions = Transaction.objects.order_by('t_date')
    context = {'transactions':transactions}
    return render(req, 'split_app/transactions.html', context)

def transaction(req, transaction_id):
    """Show single transaction"""
    transaction = Transaction.objects.get(id=transaction_id)
    obligations = Obligation.objects.filter(transaction=transaction_id)
    context = {'transaction': transaction, 'obligations':obligations}
    return render(req, 'split_app/transaction.html', context)
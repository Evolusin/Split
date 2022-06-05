from django.shortcuts import render, redirect
from .models import Transaction, Obligation
from .forms import TransactionForm
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

def new_transaction(request):
    """Adds new transaction from form"""
    if request.method != 'POST':
        # no data submitted, create a blank form
        form = TransactionForm()
    else:
        # POST submit
        form = TransactionForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('split_app:transactions')

    context = {'form':form}
    return render(request, 'split_app/new_transaction.html',context)
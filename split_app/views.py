from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Transaction, Obligation
from .forms import TransactionForm, ObligationForm
# Create your views here.
def index(req):
    return render(req,'split_app/index.html')

@login_required
def transactions(req):
    "Show all transactions"
    transactions = Transaction.objects.filter(Q(obligation__user=req.user) | Q(obligation__isnull=True))
    context = {'transactions':transactions}
    return render(req, 'split_app/transactions.html', context)

@login_required
def transaction(req, transaction_id):
    """Show single transaction"""
    transaction = Transaction.objects.get(id=transaction_id)
    obligations = Obligation.objects.filter(transaction=transaction_id)
    context = {'transaction': transaction, 'obligations':obligations}
    return render(req, 'split_app/transaction.html', context)

@login_required
def new_transaction(request):
    """Adds new transaction from form"""
    if request.method != 'POST':
        # no data submitted, create a blank form
        form = TransactionForm()
    else:
        # POST submit
        form = TransactionForm(data=request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.owner = request.user
            new_transaction.save()
            # form.save()
            return redirect('split_app:Transactions')

    context = {'form':form}
    return render(request, 'split_app/new_transaction.html',context)

@login_required
def new_obligation(request, transaction_id):
    """Adds new obligation"""
    # transaction = Transaction.objects.get(id=transaction_id)
    transaction = Transaction.objects.get(id=transaction_id)
    if transaction.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = ObligationForm()
    else:
        form = ObligationForm(data=request.POST)
        if form.is_valid():
            new_obligation = form.save(commit=False)
            new_obligation.transaction = transaction
            new_obligation.save()
            return redirect('split_app:transaction', transaction_id=transaction_id)
    context = {'transaction':transaction,'form':form}
    return render(request,'split_app/new_obligation.html', context)

@login_required
def edit_obligation(request, obligation_id):
    """Edits obligation"""
    obligation = Obligation.objects.get(id=obligation_id)
    transaction = obligation.transaction
    if transaction.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = ObligationForm(instance=obligation)
    else:
        form = ObligationForm(instance=obligation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('split_app:transaction', transaction_id = transaction.id)

    context = {'obliagtion':obligation,'transaction':transaction, 'form':form}
    return render(request,'split_app/edit_obligation.html', context)





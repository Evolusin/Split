from django.shortcuts import render, redirect
from django.db.models import Q, F
from django.utils import timezone, dateformat
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Transaction, Obligation
from users.models import Profile
from .forms import TransactionForm, ObligationForm


# Create your views here.
def index(req):
    if req.user.is_authenticated:
        profile = Profile.objects.get(user=req.user)
        context = {"profile":profile}
        return render(req, "split_app/index.html", context)
    else:
        return render(req, "split_app/index.html")


def index2(req):
    if req.user.is_authenticated:
        profile = Profile.objects.get(user=req.user)
        context = {"profile":profile}
        return render(req, "split_app/index2.html", context)
    else:
        return render(req, "split_app/index2.html")


@login_required
def transactions(req):
    "Show all owner active transactions"
    transactions_view = Transaction.objects.filter(
        (
            # (Q(obligation__user=req.user) & Q(obligation__o_status="New"))|
            ((Q(obligation__isnull=True) & Q(owner=req.user)) | Q(owner=req.user))
            & Q(t_status="New")
        )
    ).distinct()
    context = {"transactions": transactions_view}
    return render(req, "split_app/transactions.html", context)


@login_required
def topay_transactions(req):
    """Show all active transactions assign to owner/user"""
    qs_topay_transactions = Transaction.objects.filter(
        (
            (Q(obligation__user=req.user) & Q(obligation__o_status="New"))
            # | ((Q(obligation__isnull=True) & Q(owner=req.user)) | Q(owner=req.user))
            & Q(t_status="New")
        )
    ).distinct()
    context = {"qs_topay_transactions": qs_topay_transactions}
    return render(req, "split_app/topay_transactions.html", context)


@login_required
def transactions_archive(req):
    """Show all finished transactions assigned to owner/user"""
    transactions = Transaction.objects.filter(
        (
            (((Q(obligation__isnull=False) & Q(owner=req.user)) | Q(owner=req.user))
            & Q(t_status="Done")) | ((Q(obligation__user=req.user) | Q(owner=req.user)) & Q(obligation__o_status='Done'))
        )
    ).distinct()
    owner = Transaction.owner
    t_desc = Transaction.t_desc
    profile = Profile.user
    context = {"transactions": transactions, "owner": owner, "t_desc": t_desc, "profile": profile}
    return render(req, "split_app/transactions_archive.html", context)


@login_required
def transaction(req, transaction_id):
    """Show single active transaction for owner"""
    transaction = Transaction.objects.get(id=transaction_id)
    obligations = Obligation.objects.filter(
        Q(transaction=transaction_id) & Q(o_status="New")
    )
    profile = Profile.user
    context = {"transaction": transaction, "obligations": obligations}
    return render(req, "split_app/transaction.html", context)

@login_required
def topay_transaction(req, transaction_id):
    """Show single active qs_transaction for obligation user to pay"""
    qs_transaction = Transaction.objects.get(id=transaction_id)
    obligations = Obligation.objects.filter(Q(transaction=transaction_id) & Q(o_status="New"))
    profile = Profile.user
    context = {"qs_transaction": qs_transaction, "obligations": obligations}
    return render(req, "split_app/topay_transaction.html", context)


@login_required
def transaction_a(req, transaction_id):
    """Show single archived transaction"""
    transaction_a = Transaction.objects.get(id=transaction_id)
    obligations = Obligation.objects.filter(
        Q(transaction=transaction_id) & Q(o_status="Done")
    )
    profile = Profile.user
    context = {"transaction_a": transaction_a, "obligations": obligations, 'profile': profile}
    return render(req, "split_app/transaction_a.html", context)


@login_required
def new_transaction(request):
    """Adds new transaction from form"""
    if request.method != "POST":
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
            return redirect("split_app:Transactions")

    context = {"form": form}
    return render(request, "split_app/new_transaction.html", context)


@login_required
def new_obligation(request, transaction_id):
    """Adds new obligation"""
    # transaction = Transaction.objects.get(id=transaction_id)
    transaction = Transaction.objects.get(id=transaction_id)
    if transaction.owner != request.user:
        raise Http404
    if request.method != "POST":
        form = ObligationForm()
    else:
        form = ObligationForm(data=request.POST)
        if form.is_valid():
            new_obligation = form.save(commit=False)
            new_obligation.transaction = transaction

            new_obligation.save()
            return redirect("split_app:transaction", transaction_id=transaction_id)
    context = {"transaction": transaction, "form": form}
    return render(request, "split_app/new_obligation.html", context)


@login_required
def edit_obligation(request, obligation_id):
    """Edits obligation"""
    obligation = Obligation.objects.prefetch_related("transaction").get(
        id=obligation_id
    )
    transaction = obligation.transaction

    if transaction.owner != request.user:
        raise Http404
    if request.method != "POST":
        form = ObligationForm(instance=obligation)
    else:
        form = ObligationForm(instance=obligation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("split_app:transaction", transaction_id=transaction.id)

    context = {"obliagtion": obligation, "transaction": transaction, "form": form}
    return render(request, "split_app/edit_obligation.html", context)

@login_required
def delete_obligation(request, obligation_id):
    """Allows owner of transaction to delete obligation"""
    qs_obliagtion = Obligation.objects.get(id=obligation_id)
    if qs_obliagtion.transaction.owner != request.user:
        raise Http404
    else:
        qs_obliagtion.delete()
        return redirect("split_app:transaction", transaction_id=qs_obliagtion.transaction.id)


@login_required
def pay_obligation(request, obligation_id, transaction_id):
    """Pays the obligations. Only user who is in debt can pay for it"""
    obligation = Obligation.objects.get(id=obligation_id)
    transaction = Transaction.objects.get(id=transaction_id)
    o = Obligation.objects.filter(Q(transaction_id=transaction.id) & Q(o_status="New"))
    obligation.o_status = "Done"
    obligation.payment_date = dateformat.format(timezone.now(), 'Y-m-d')
    transaction.t_status = "Done"
    obligation.save(update_fields=["o_status", "payment_date"])
    if not o:
        transaction.save(update_fields=["t_status"])

    return redirect("split_app:topay_transactions")

@login_required
def edit_transaction(request,transaction_id):
    """Allows editing transaction by owner"""
    var_transaction = Transaction.objects.get(id=transaction_id)
    if var_transaction.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = TransactionForm(instance=var_transaction)
    else:
        form = TransactionForm(instance=var_transaction, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("split_app:transaction", transaction_id=var_transaction.id)

    context = {"var_transaction": var_transaction, "form": form}
    return render(request, "split_app/edit_transaction.html", context)

@login_required
def delete_transaction(request, transaction_id):
    """Allows owner of transaction to delete transaction"""
    qs_transaction = Transaction.objects.get(id=transaction_id)
    if qs_transaction.owner != request.user:
        raise Http404
    else:
        qs_transaction.delete()
        return redirect("split_app:Transactions")


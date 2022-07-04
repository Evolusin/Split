from django.urls import path
from . import views

app_name = "split_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("transactions/", views.transactions, name="Transactions"),
    path("transactions_archive/", views.transactions_archive, name="Transactions_archive"),
    path("transactions_archive/<int:transaction_id>/", views.transaction_a, name="transaction_a"),
    path("transactions/<int:transaction_id>/", views.transaction, name="transaction"),
    path("new_transaction/", views.new_transaction, name="new_transaction"),
    path(
        "new_obligation/<int:transaction_id>/",
        views.new_obligation,
        name="new_obligation",
    ),
    path(
        "edit_obligation/<int:obligation_id>",
        views.edit_obligation,
        name="edit_obligation",
    ),
    path(
        "pay_obligation/<int:obligation_id>/<int:transaction_id>",
        views.pay_obligation,
        name="pay_obligation",
    ),
]

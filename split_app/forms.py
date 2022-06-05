from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    t_date = DateTimeField
    class Meta:
        model = Transaction
        model.t_date = forms.IntegerField()
        fields = ['owner','t_desc','t_date']
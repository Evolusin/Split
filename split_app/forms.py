from django import forms
from .models import Transaction, Obligation
from datetime import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class TransactionForm(forms.ModelForm):
    t_date = forms.DateField(initial=datetime.today(), label='Kiedy')
    class Meta:
        model = Transaction
        fields = ['owner','t_desc','t_date']
        widgets = {
            't_date': DateInput()
        }
        labels = {
            'owner':'Kto stawiał?','t_desc':'Za co?'
        }

class ObligationForm(forms.ModelForm):
    class Meta:
        model = Obligation
        fields = ['transaction','user', 'desc', 'value', 'optional_value']


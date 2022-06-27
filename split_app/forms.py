from django import forms
from .models import Transaction, Obligation
from datetime import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class TransactionForm(forms.ModelForm):
    t_date = forms.DateField(initial=datetime.today(), label='Kiedy')
    class Meta:
        model = Transaction
        fields = ['t_desc','t_date']
        widgets = {
            't_date': DateInput()
        }
        labels = {
            't_desc':'Za co?'
        }

class ObligationForm(forms.ModelForm):
    class Meta:
        model = Obligation
        fields = ['transaction','user', 'desc', 'value', 'optional_value']
        labels = {
            'transaction':'Który split','user': 'Winny', 'desc': 'Za co?', 'value':'Ile zł', 'optional_value':'Koszty dodatkowe'
        }
        widgets = {
            'desc':forms.Textarea(attrs={'rows':2,'cols':20})
        }


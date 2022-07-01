from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UPasswordChange(forms.ModelForm):
    """Form that lets user change their password"""
    class Meta:
        model = User
        fields = ["password","password"]
        labels = {
            "password": "Hasło",
        }
        # widgets = {"desc": forms.Textarea(attrs={"rows": 2, "cols": 20})}
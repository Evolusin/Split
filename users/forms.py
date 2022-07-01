from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core.exceptions import ValidationError

class UPasswordChange(forms.ModelForm):
    """Form that lets user change their password"""
    class Meta:
        model = User
        fields = ['username','password']

# class login(login):
#     """Form (child class from django auth) that lets user input theirs login and password"""
#     class Meta:
#         model = User
#         # fields = ['username','password']
#         fields = '__all__'
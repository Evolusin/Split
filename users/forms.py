from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import PasswordChangeForm

class UPasswordChange(PasswordChangeForm):
    old_password = forms.CharField(
        label=("Old te"))
    class Meta:
        model = User
    #     print('test')
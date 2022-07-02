from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordChangeForm


class UPasswordChange(PasswordChangeForm):

    class Meta:
        model = User
        fields = 'old_password'
    #     print('test')

from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm


class UPasswordChange(PasswordChangeForm):
    class Meta:
        model = User

    #     print('test')

    def __init__(self, *args, **kwargs):
        super(UPasswordChange, self).__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["nick", "phone", "bank"]
        labels = {
            "nick":"Nick",
            "phone":"Nr telefonu",
            "bank":"Nr konta bankowego",
        }
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import UPasswordChange
from django.contrib.auth.models import User

# Create your views here.



def upassword_change(request):
    """Allows users to change his password"""
    # print(user)
    if request.method != 'POST':
        form = UPasswordChange(request.user)
    else:
        form = UPasswordChange(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Hasło zmienione')
            return redirect('split_app:upassword_change')

    context = {'form': form}
    return render(request, 'registration/password_change.html', context)
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UPasswordChange
from django.contrib.auth.models import User

# Create your views here.

# def login(login)

def upassword_change(request):
    """Allows users to change his password"""
    # print(user)
    user = request.user.id
    if request.method != 'POST':
        form = UPasswordChange(request.POST)
    else:
        form = UPasswordChange(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Hasło zmienione')
            return redirect('split_app:upassword_change')

    context = {'form': form, 'user':user}
    return render(request, 'registration/upassword_change.html', context)
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import UPasswordChange
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    """Allows to register new user"""
    if request.method != 'POST':
        # No data submitted -> create form
        form = UserCreationForm
    else:
        # POST submit
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in and redirect to home page
            login(request, new_user)
            return redirect('split_app:index')

    # Display a blank/invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def upassword_change(request, user_id):
    """Allows users to change his password"""
    # print(user)
    user = User.objects.get(user_id)
    print(user)
    if request.method != 'POST':
        form = UPasswordChange(request.user)
    else:
        form = UPasswordChange(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Hasło zmienione')
            return redirect('split_app:index')

    context = {'form': form}
    return render(request, 'registration/password_change.html', context)
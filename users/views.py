from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import UPasswordChange

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

def upassword_change(request):
    """Allows users to change his password"""
    if request.method != 'POST':
        form = UPasswordChange
    else:
        form = UPasswordChange(data=request.POST)
        if form.is_valid():
            password = form.save()
            # return redirect('split_app:index')

    context = {'form': form}
    return render(request, 'registration/password_change.html', context)
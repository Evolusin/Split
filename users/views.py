from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


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

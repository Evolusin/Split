from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UPasswordChange, EditProfile
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Profile

# Create your views here.


@login_required
def upassword_change(request):
    """Allows users to change his password"""
    user = request.user
    if request.method != 'POST':
        form = UPasswordChange(user=user)
    else:
        form = UPasswordChange(data=request.POST, user=user)
        if form.is_valid():
            form.save()
            # messages.success(request,'Hasło zmienione')
            return redirect('split_app:index')
        else:
            print(form.error_messages)

    context = {'form': form, 'user':user}
    return render(request, 'registration/upassword_change.html', context)


@login_required
def profile(request, user_id):
    """Shows profile"""
    profile_var = Profile.objects.get(user=request.user, user_id=request.user.id)
    context = {"profile": profile_var}
    return render(request, "registration/profile.html", context)


@login_required
def editprofile(request, user_id):
    """Allows to edit profile by loggged user"""
    eprofile = Profile.objects.get(user=request.user, user_id=request.user.id)
    if request.method != "POST":
        form = EditProfile(instance=eprofile)
    else:
        form = EditProfile(instance=eprofile, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:profile", user_id=eprofile.user_id)

    context = {"eprofile":eprofile, "form":form}
    return render(request, "registration/edit_profile.html", context)

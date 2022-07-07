from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UPasswordChange
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Profile

# Create your views here.


@login_required
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
            return redirect('split_app:index')

    context = {'form': form, 'user':user}
    return render(request, 'registration/upassword_change.html', context)

@login_required
def profile(request, user_id):
    """Shows profile"""
    profile_var = Profile.objects.get(user=request.user, user_id=request.user.id)
    context = {"profile": profile_var}
    return render(request, "registration/profile.html", context)
# @login_required
# def edit_profile(request):
#     """Edit profile by user who is currently logged"""
#     profile = Profile.objects.get(user=request.user)
#
#     if profile.user != request.user:
#         raise Http404
#     if request.method != "POST":
#         form = ObligationForm(instance=profile)
#     else:
#         form = ObligationForm(instance=profile, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("split_app:index", transaction_id=transaction.id)
#
#     context = {"profile": profile, "form": form}
#     return render(request, "split_app/edit_obligation.html", context)
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# from django.http import HttpResponseRedirect
# from django.urls import reverse

# Create your models here.

# class PasswordChange(models.Model):
#     """This middleware checks if the user requires a password change and if he needs then forces him to change it"""
#     def __init__(self):
#         self.get_response = get_response
#
#     def __call__(self, request):

class Profile(models.Model):
    """Profiles that expands built-in User class in Django.
     Adds firstnames/lastnames/emails/phone number (used in payment by BLIK)"""
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    nick = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=50, null=False, blank=False)
    pass_change_force = models.BooleanField(default=True)
    phone = models.IntegerField(null=True, blank=True, unique=True)

    def __str__(self):
        return f"{self.user} - {self.first_name} - {self.last_name} - {self.email}"

    def spaced_format(value):
        left = int(value / 10000)
        right = value % 10000
        return '{:03} {:04}'.format(left, right)

class UUser(User):
    Psignal = models.BooleanField(default=False)
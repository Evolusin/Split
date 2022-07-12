from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# from django.http import HttpResponseRedirect
# from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    """Profiles that expands built-in User class in Django.
     Adds firstnames/lastnames/emails/phone number (used in payment by BLIK)"""
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=40, null=False, blank=False)
    last_name = models.CharField(max_length=40, null=False, blank=False)
    nick = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=50, null=False, blank=False)
    pass_change_force = models.BooleanField(default=True)
    phone = models.IntegerField(null=True, blank=True, unique=True)
    bank = models.CharField(default='-', max_length=255)

    def __str__(self):
        return f"{self.user} - {self.first_name} - {self.last_name} - {self.email}"


class UUser(User):
    Psignal = models.BooleanField(default=False)
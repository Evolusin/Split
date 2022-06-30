from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your models here.

# class PasswordChange(models.Model):
#     """This middleware checks if the user requires a password change and if he needs then forces him to change it"""
#     def __init__(self):
#         self.get_response = get_response
#
#     def __call__(self, request):

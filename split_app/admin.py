from django.contrib import admin
from .models import Transaction, Obligation
from users.models import Profile

# Register your models here.

admin.site.register(Transaction)
admin.site.register(Obligation)
admin.site.register(Profile)

from django.contrib import admin
from .models import Transaction, Obligation

# Register your models here.

admin.site.register(Transaction)
admin.site.register(Obligation)

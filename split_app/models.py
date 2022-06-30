import django.utils.timezone
from django.db import models
from django.contrib.auth.models import User
import split_app.choices as c

# Create your models here.


class Transaction(models.Model):
    """A transaction that person starts"""

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    t_desc = models.TextField(blank=True, null=True)
    t_date = models.DateField()
    t_status = models.CharField(default=c.new, editable=False, max_length=16)

    def __str__(self):
        return f"{self.owner} - {self.t_date} - {self.t_desc}"


class Obligation(models.Model):
    transaction = models.ForeignKey(
        Transaction, related_name="obligation", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.TextField(blank=True, null=True)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    optional_value = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    o_status = models.CharField(default=c.new, choices=c.status, max_length=16)
    payment_date = models.DateField(
        default=django.utils.timezone.now, null=True, blank=True
    )

    def __str__(self):
        return f"{self.desc} - {self.value} - {self.payment_date} - {self.user}"

    @property
    def suma(self):
        if self.optional_value:
            return self.value + self.optional_value
        return self.value

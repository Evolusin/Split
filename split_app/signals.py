from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Profile
from .models import Obligation


@receiver(post_save, sender=Obligation)
def obligation_notification(sender, created, **kwargs):
    if created:
        print("Stworzono nową należność")
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Profile
from .models import Obligation
import gmail


@receiver(post_save, sender=Obligation)
def obligation_notification(sender, instance, created, **kwargs):
    if created:
        print("Stworzono nową należność")
        qs_profile = Profile.objects.get(user=instance.user.id)
        qs_obligation = Obligation.objects.get(id=instance.id)
        print(qs_profile.email)
        print(qs_profile.first_name)
        print(qs_profile.last_name)
        html = "https://splitappsaventic.herokuapp.com/"
        msg = f"""
        Cześć {qs_profile.first_name}, ktoś dodał właśnie na Splita należność o wartości {qs_obligation.suma} zł do spłacenia.
        Zaloguj się do aplikacji na {html} aby sprawdzić szczegóły
        """
        gmail.prepare_email(msg)
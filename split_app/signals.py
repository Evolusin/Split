from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Profile
from .models import Obligation
from split_app.gmail import prepare_email


@receiver(post_save, sender=Obligation)
def obligation_notification(sender, instance, created, **kwargs):
    if created:
        print("Stworzono nową należność")
        qs_profile = Profile.objects.get(user=instance.user.id)
        qs_obligation = Obligation.objects.get(id=instance.id)
        print(qs_profile.email)
        print(qs_profile.first_name)
        print(qs_profile.last_name)
        site = "https://splitappsaventic.herokuapp.com/"
        body = f"""
Cześć {qs_profile.first_name}!
Użytkownik {qs_obligation.transaction.owner.profile.first_name} {qs_obligation.transaction.owner.profile.last_name} dodał właśnie na Splita należność o wartości {qs_obligation.suma} zł do spłacenia.
Za co - {qs_obligation.transaction.t_desc}

Zaloguj się do aplikacji na {site} aby sprawdzić szczegóły

Split Saventic
        """
        prepare_email(qs_profile.email, body)

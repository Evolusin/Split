from django.apps import AppConfig



class SplitAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "split_app"

    def ready(self):
        import split_app.signals

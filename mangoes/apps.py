from django.apps import AppConfig


class MangoesConfig(AppConfig):
    name = 'mangoes'

    def ready(self):
        import mangoes.signals

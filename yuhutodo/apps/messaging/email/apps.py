from django.apps import AppConfig


class EmailConfig(AppConfig):
    name = 'yuhutodo.apps.messaging.email'

    def ready(self):
        pass

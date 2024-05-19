from django.apps import AppConfig
from django.db.models.signals import post_save


class TodoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "yuhutodo.apps.todo"

    def ready(self):
        from yuhutodo.apps.todo.models import Todo
        from yuhutodo.apps.todo.signals import notify_action

        post_save.connect(notify_action, sender=Todo)

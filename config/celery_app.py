import os

from celery import Celery
from celery.schedules import crontab

from yuhutodo.apps.todo.helpers import mark_task_as_expired

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

app = Celery("yuhutodo")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # TODO: verificar esto
    from django.contrib.auth import get_user_model

    User = get_user_model()
    # periodic task to run every day in the midnight
    users = User.objects.all()
    for user in users:
        sender.add_periodic_task(
            crontab(hour=0, minute=1),
            verify_expiration.s("test"),
            name="mark expired tasks",
        )


@app.task
def test(args):
    pass


@app.task
def verify_expiration(*args):
    """
    Mark tasks as expired
    """
    print("Running task")
    # mark_task_as_expired(user_id)

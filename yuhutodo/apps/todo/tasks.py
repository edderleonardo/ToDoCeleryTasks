# crate task when user add a new Task

from celery import shared_task

from yuhutodo.apps.messaging.email.helpers import send_email


@shared_task
def send_email_notification(action: str, title: str, description: str, email: str):
    """
    Send email when a new task is created
    """
    title_email = "Nueva tarea creada" if action == "created" else "Tarea actualizada"

    send_email(
        subject=title_email,
        to_email=[email],
        template="emails/notify_tasks/notify.html",
        ctx={
            "title": title_email,
            "title_task": title,
            "description": description,
        },
    )

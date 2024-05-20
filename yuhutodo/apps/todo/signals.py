from yuhutodo.apps.todo.tasks import send_email_notification


def notify_action(sender, instance, created, **kwargs):
    """
    Send email notification when a new task is created
    """
    action = "created" if created else "updated"
    title = instance.title
    description = instance.description
    email = instance.user.email
    send_email_notification.delay(action=action, title=title, description=description, email=email)

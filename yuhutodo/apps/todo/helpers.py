def mark_task_as_expired(user_id):
    """
    Mark tasks as expired
    """
    from django.contrib.auth import get_user_model

    from yuhutodo.apps.todo.models import Todo

    User = get_user_model()

    try:
        user = User.objects.get(id=user_id)
        todos = Todo.objects.get_current_user_tasks(user).get_expired_tasks()
        for todo in todos:
            todo.expired_task = True
            todo.save()
    except User.DoesNotExist:
        print("User does not exist")

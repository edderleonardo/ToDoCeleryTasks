from django.contrib.auth import get_user_model
from django.db.models import CASCADE
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import ForeignKey
from django.db.models import QuerySet
from django.db.models import TextField
from django.utils import timezone

from yuhutodo.apps.core.models import TimeStampedModel

User = get_user_model()


class TodoQuerySet(QuerySet):
    def get_current_user_tasks(self, user):
        """
        Return tasks for the current authenticated user
        """
        return self.filter(user=user)

    def get_expired_tasks(self):
        """
        Return expired tasks
        """
        return self.filter(due_date__lt=timezone.now(), expired_task=False).exclude(
            is_completed=True,
        )


class Todo(TimeStampedModel):
    title = CharField(max_length=255)
    description = TextField(blank=True)
    is_completed = BooleanField(default=False)
    due_date = DateTimeField(blank=True, null=True)
    user = ForeignKey(User, on_delete=CASCADE)
    expired_task = BooleanField(default=False)

    objects = TodoQuerySet.as_manager()

    def __str__(self):
        return f"{self.title} - {self.user}"

from django.contrib.auth import get_user_model
from django.db.models import CASCADE
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import ForeignKey
from django.db.models import TextField

from yuhutodo.apps.core.models import TimeStampedModel

User = get_user_model()


class Todo(TimeStampedModel):
    title = CharField(max_length=255)
    description = TextField(blank=True)
    is_completed = BooleanField(default=False)
    due_date = DateTimeField(blank=True, null=True)
    user = ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return f"{self.title} - {self.user}"

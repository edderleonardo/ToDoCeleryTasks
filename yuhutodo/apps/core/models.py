from django.db.models import DateTimeField
from django.db.models import Model


class TimeStampedModel(Model):
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

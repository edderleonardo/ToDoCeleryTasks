from rest_framework import serializers

from yuhutodo.apps.todo.models import Todo


class TodoSerializer(serializers.ModelSerializer[Todo]):
    class Meta:
        model = Todo
        fields = [
            "id",
            "title",
            "description",
            "is_completed",
            "due_date",
            "expired_task",
        ]

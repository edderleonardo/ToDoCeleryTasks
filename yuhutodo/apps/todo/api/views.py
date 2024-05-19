from rest_framework import viewsets

from yuhutodo.apps.todo.models import Todo

from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    lookup_field = "pk"

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from rest_framework import viewsets

from yuhutodo.apps.todo.models import Todo

from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    # TODO: Get only the todos of the authenticated user
    # queryset = Todo.objects.all()
    lookup_field = "pk"

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

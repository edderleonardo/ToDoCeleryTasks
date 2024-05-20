from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from yuhutodo.apps.todo.models import Todo

from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    lookup_field = "pk"
    pagination_class = PageNumberPagination


    def perform_create(self, serializer):
        """
        Save user logged in user when creating a new task

        Author:
            Edder Ramírez
        """
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        Return tasks for the current authenticated user

        Author:
            Edder Ramírez
        """
        return Todo.objects.filter(user=self.request.user)

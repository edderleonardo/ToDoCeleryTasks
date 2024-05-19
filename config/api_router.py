from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from yuhutodo.apps.todo.api.views import TodoViewSet
from yuhutodo.apps.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("tasks", TodoViewSet, basename="todo")


app_name = "api"
urlpatterns = router.urls

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class TodoView(LoginRequiredMixin, TemplateView):
    template_name = "pages/todo.html"

from django.views.generic import TemplateView


class TodoView(TemplateView):
    template_name = "pages/todo.html"

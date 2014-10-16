from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from django.views.generic import TemplateView

from home.models import Todo
from home.serializers import TodoSerializer


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        return {"current_page_name": "Home"}


class TodoMixin(object):
    queryset = Todo.objects.all().order_by('-id')
    serializer_class = TodoSerializer
    parser_classes = (JSONParser,)


class TodoList(TodoMixin, ListCreateAPIView):
    """Return a list of all the todos, or create new ones."""
    pass


class TodoDetail(TodoMixin, RetrieveUpdateDestroyAPIView):
    """Return a specific todo, update it, or delete it."""
    pass

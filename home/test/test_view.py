import json
from nose.plugins.attrib import attr
from rest_framework import status

from django.core.urlresolvers import reverse
from django.test import TestCase

from home.models import Todo


@attr('integration')
class HomeViewTest(TestCase):

    def setUp(self):
        self.url = reverse('home:home_page')

    def test_simple_home_view(self):
        response = self.client.get(
            self.url,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.context.get('current_page_name'), 'Home')


@attr('integration')
class TodoViewTest(TestCase):

    def setUp(self):
        Todo.objects.create(item='testFalse', is_done=False)
        Todo.objects.create(item='testTrue', is_done=True)
        self.get_url = reverse('home:todos_list')
        self.update_url = reverse('home:todos_update', kwargs={"pk": 1})

    def test_get_todos(self):
        response = self.client.get(
            self.get_url,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0], {"item": u"testFalse", "is_done": False, "id": 1})
        self.assertEqual(response.data[1], {"item": u"testTrue", "is_done": True, "id": 2})
        self.assertEqual(len(response.data), 2)

    def test_add_todo(self):
        response = self.client.post(
            self.get_url,
            data={
                'item': "My favorite todo",
                'is_done': False
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(
            self.get_url,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0], {"item": u"testFalse", "is_done": False, "id": 1})
        self.assertEqual(response.data[1], {"item": u"testTrue", "is_done": True, "id": 2})
        self.assertEqual(response.data[2], {"item": u"My favorite todo", "is_done": False, "id": 3})
        self.assertEqual(len(response.data), 3)

    def test_update_todo(self):
        response = self.client.put(
            self.update_url,
            data=json.dumps({
                'item': "testFalse is now True",
                'is_done': True,
                'id': 1,
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(
            self.get_url,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0], {"item": u"testFalse is now True", "is_done": True, "id": 1})
        self.assertEqual(response.data[1], {"item": u"testTrue", "is_done": True, "id": 2})
        self.assertEqual(len(response.data), 2)

    def test_delete_todo(self):
        response = self.client.delete(
            self.update_url,
            data=json.dumps({
                'id': 1,
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(
            self.get_url,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0], {"item": u"testTrue", "is_done": True, "id": 2})
        self.assertEqual(len(response.data), 1)
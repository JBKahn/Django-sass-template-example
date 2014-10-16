from rest_framework import status

from django.core.urlresolvers import reverse
from django.test import TestCase
from nose.plugins.attrib import attr


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

from django.http import HttpRequest
from django.test import TestCase

# Create your tests here.
from django.urls import resolve
from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)

    def test_users_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
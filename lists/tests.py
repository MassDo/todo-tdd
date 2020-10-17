from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        my_view = resolve('/')
        self.assertEqual(my_view.func, home_page)

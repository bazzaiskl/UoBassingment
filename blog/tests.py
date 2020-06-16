from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from blog.views import post_list
from blog.models import CV

# Create your tests here.
class HomePageTest(TestCase):
    def test_form_filled(self):
        CV.name = "bob"
        self.assertEqual("bob",CV.name)
        



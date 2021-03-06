from django.test import TestCase
from django.urls import resolve 
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string



# Create your tests here.
class HomePageTest(TestCase):

    def test_resolveRootUrl(self):
        #resolve root URL as home page
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_homePageContent(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_POSTRequest(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

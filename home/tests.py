# Test code from Claude AI
from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):

    def test_home_page_loads(self):
        """Test that the home page returns 200"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        """Test that the home page uses the correct template"""
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home/index.html')

    def test_about_page_loads(self):
        """Test that the about page returns 200"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_loads(self):
        """Test that the contact page returns 200"""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
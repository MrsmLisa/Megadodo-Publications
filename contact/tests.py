# Test code from Claude AI
from django.test import TestCase
from django.urls import reverse
from .models import Contact


class ContactModelTest(TestCase):

    def test_contact_page_loads(self):
        """Test that the contact page returns 200"""
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_form_submission(self):
        """Test that a contact form submission works"""
        response = self.client.post(reverse('contact'), {
            'name': 'Test User',
            'email': 'test@test.com',
            'subject': 'Test Subject',
            'message': 'Test message',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Contact.objects.count(), 1)

    def test_contact_model_str(self):
        """Test contact string representation"""
        contact = Contact.objects.create(
            name='Test User',
            email='test@test.com',
            subject='Test Subject',
            message='Test message',
        )
        self.assertEqual(str(contact), 'Test User - Test Subject')
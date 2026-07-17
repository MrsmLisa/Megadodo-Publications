# Test code from Claude AI
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile


class ProfileViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_profile_requires_login(self):
        """Test that the profile page requires login"""
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)

    def test_profile_loads_when_logged_in(self):
        """Test that the profile page loads for logged in user"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_profile_created_on_user_creation(self):
        """Test that a profile is created when a user is created"""
        self.assertTrue(
            UserProfile.objects.filter(user=self.user).exists()
        )
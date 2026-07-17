# Test code from Claude AI
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Question, Answer


class ForumViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.question = Question.objects.create(
            question='Test Question?',
            created_by=self.user
        )

    def test_forum_page_loads(self):
        """Test that the forum page returns 200"""
        response = self.client.get(reverse('forum'))
        self.assertEqual(response.status_code, 200)

    def test_question_detail_loads(self):
        """Test that the question detail page returns 200"""
        response = self.client.get(
            reverse('question_detail', args=[self.question.pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_create_question_requires_login(self):
        """Test that creating a question requires login"""
        response = self.client.get(reverse('create_question'))
        self.assertEqual(response.status_code, 302)

    def test_create_question_logged_in(self):
        """Test that a logged in user can create a question"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('create_question'), {
            'question': 'New test question?',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Question.objects.count(), 2)

    def test_question_str(self):
        """Test question string representation"""
        self.assertEqual(str(self.question), 'Test Question?')
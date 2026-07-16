from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    question = models.CharField(max_length=300)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        # Orders questions by creation date, newest first
        ordering = ['-created_at']


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='answers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Display the first 50 characters of the answer
        return f'Answer to: {self.question.question}'

    class Meta:
        # Orders answers by creation date, newest first
        ordering = ['-created_at']

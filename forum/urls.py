from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('question/create/', views.create_question, name='create_question'),
    path('question/<int:question_id>/edit/', views.edit_question, name='edit_question'),
    path('question/<int:question_id>/delete/', views.delete_question, name='delete_question'),
    path('question/<int:question_id>/answer/', views.create_answer, name='create_answer'),
    path('answer/<int:answer_id>/edit/', views.edit_answer, name='edit_answer'),
    path('answer/<int:answer_id>/delete/', views.delete_answer, name='delete_answer'),
]
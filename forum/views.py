from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from django.contrib import messages

# Create your views here.

def forum(request):
    questions = Question.objects.all()
    return render(request, 'forum/forum.html', {'questions': questions})

def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answers.all()
    return render(request, 'forum/question_detail.html', {
        'question': question, 
        'answers': answers
    })


@login_required
def create_question(request):
    if request.method == 'POST':
        question_text = request.POST.get('question')
        Question.objects.create(
            question=question_text, 
            created_by=request.user
        )
        messages.success(request, 'Your question has been posted.')
        return redirect('forum')
    return render(request, 'forum/create_question.html')


@login_required
def edit_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if question.created_by != request.user:
        messages.error(request, 'You can only edit your own questions.')
        return redirect('forum')
    if request.method == 'POST':
        question_text = request.POST.get('question')
        question.question = question_text
        question.save()
        messages.success(request, 'Your question has been updated.')
        return redirect('forum')
    return render(request, 'forum/edit_question.html', {'question': question})


@login_required
def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if question.created_by != request.user:
        messages.error(request, 'You can only delete your own questions.')
        return redirect('forum')
    if request.method == 'POST':
        question.delete()
        messages.success(request, 'Your question has been deleted.')
        return redirect('forum')
    return render(request, 'forum/delete_question.html', {'question': question})


@login_required
def create_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        answer_text = request.POST.get('answer')
        Answer.objects.create(
            question=question, 
            answer=answer_text, 
            created_by=request.user
        )
        messages.success(request, 'Your answer has been posted.')
        return redirect('question_detail', question_id=question.id)
    return render(request, 'forum/create_answer.html', {'question': question})


@login_required
def edit_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if answer.created_by != request.user:
        messages.error(request, 'You can only edit your own answers.')
        return redirect('forum')
    if request.method == 'POST':
        answer_text = request.POST.get('answer')
        answer.answer = answer_text
        answer.save()
        messages.success(request, 'Your answer has been updated.')
        return redirect('question_detail', question_id=answer.question.id)
    return render(request, 'forum/edit_answer.html', {'answer': answer})


@login_required
def delete_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if answer.created_by != request.user:
        messages.error(request, 'You can only delete your own answers.')
        return redirect('forum')
    if request.method == 'POST':
        question_id = answer.question.id
        answer.delete()
        messages.success(request, 'Your answer has been deleted.')
        return redirect('question_detail', question_id=question_id)
    return render(request, 'forum/delete_answer.html', {'answer': answer})
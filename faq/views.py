from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FAQ

# Create your views here.

def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq/faq.html', {'faqs': faqs})

@login_required
def create_faq(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        FAQ.objects.create(
            question=question, 
            answer=answer, 
            created_by=request.user
        )
        messages.success(request, 'FAQ created successfully.')
        return redirect('faq')
    return render(request, 'faq/create_faq.html')

@login_required
def edit_faq(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)
    if faq.created_by != request.user:
        messages.error(request, 'You can only edit your own FAQs.')
        return redirect('faq')
    if request.method == 'POST':
        faq.question = request.POST.get('question')
        faq.answer = request.POST.get('answer')
        faq.save()
        messages.success(request, 'FAQ updated successfully.')
        return redirect('faq')
    return render(request, 'faq/edit_faq.html', {'faq': faq})

@login_required
def delete_faq(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)
    if faq.created_by != request.user:
        messages.error(request, 'You can only delete your own FAQs.')
        return redirect('faq')
    faq.delete()
    messages.success(request, 'FAQ deleted successfully.')
    return redirect('faq')


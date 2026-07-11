from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

# Create your views here.


def contact_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        return render(request, 'contact/thank_you.html', {'name': name})
    form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})


def contact_read(request):
    from .models import Contact
    contacts = Contact.objects.all()
    return render(request, 'contact/contact_list.html', {'contacts': contacts})

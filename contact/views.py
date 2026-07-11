from django.shortcuts import render

# Create your views here.

def contact_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        created_at = request.POST.get('created_at') 

        from .models import Contact
        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        return render(request, 'contact/thank_you.html', {'name': name})

    return render(request, 'contact/contact_form.html')


def contact_read(request):
    from .models import Contact
    contacts = Contact.objects.all()
    return render(request, 'contact/contact_list.html', {'contacts': contacts})


def contact_update(request, contact_id):
    from .models import Contact
    contact = Contact.objects.get(id=contact_id)

    if request.method == 'POST':
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.subject = request.POST.get('subject')
        contact.message = request.POST.get('message')
        contact.save()

        return render(request, 'contact/thank_you.html', {'name': contact.name})

    return render(request, 'contact/contact_form.html', {'contact': contact})


def contact_delete(request, contact_id):
    from .models import Contact
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return render(request, 'contact/contact_list.html', {'contacts': Contact.objects.all()})


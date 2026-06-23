from django.shortcuts import render
from .models import books

# Create your views here.

def book_list(request):
    books = books.objects.all()
    return render(request, 'products/book_list.html', {'books': books})

class BookListView(ListView):
    model = books
    template_name = 'products/book_list.html'
    context_object_name = 'books'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset
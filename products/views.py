from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset
    

def product_detail(request, pk):
   product = get_object_or_404(Product, pk=pk)
   return render(request, 'products/product_detail.html', {'product' : product})
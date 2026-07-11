from django.shortcuts import render
from products.models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'home/index.html')

def about (request):
    return render(request, 'home/about.html')

def terms (request):
    return render(request, 'home/terms.html')

def delivery (request):
    return render(request, 'home/delivery.html')

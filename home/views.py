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

def index(request):
    try:
        hitchhikers = Product.objects.get(name='The Hitchhiker\'s Guide to the Galaxy')
        fifty_threes = Product.objects.get(name='53 More Things to Do in Zero Gravity')
    except Product.DoesNotExist:
        hitchhikers = None
        fifty_threes = None

    return render(request, 'home/index.html', {
        'hitchhikers': hitchhikers, 
        'fifty_threes': fifty_threes,
    })

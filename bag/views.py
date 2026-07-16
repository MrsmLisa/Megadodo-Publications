from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if str(product_id) in bag:
        bag[str(product_id)] += quantity
        messages.success
        (request, f'Updated {product.name} quantity to {bag[str(product_id)]}')
    else:
        bag[str(product_id)] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def update_bag(request, product_id):
    """ Update the quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[str(product_id)] = quantity
        messages.success
        (request, f'Updated {product.name} quantity to {bag[str(product_id)]}')
    else:
        bag.pop(str(product_id), None)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect('view_bag')


def remove_from_bag(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    bag = request.session.get('bag', {})
    bag.pop(str(product_id), None)
    messages.success(request, f'Removed {product.name} from your bag')
    request.session['bag'] = bag
    return redirect('view_bag')

from decimal import Decimal

from django.conf import settings
from products.models import Product

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for product_id, quantity in bag.items():
        product = Product.objects.get(pk=product_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
            'subtotal': quantity * product.price,
        })

    free_delivery_threshold = settings.FREE_DELIVERY_THRESHOLD

    if total >= free_delivery_threshold:
        delivery = 0
        free_delivery_delta = 0
    else:
        delivery = Decimal('4.99')  # Flat rate delivery charge
        free_delivery_delta = free_delivery_threshold - total

    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': free_delivery_threshold,
        'grand_total': grand_total,
    }    
    
    return context
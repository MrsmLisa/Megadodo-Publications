from profile import Profile
from pyexpat.errors import messages

from django.shortcuts import render, get_object_or_404
from oauthlib.uri_validate import query

from profiles.models import UserProfile
from .models import Product
from django.views.generic import ListView
from django.db.models import Q
from contact.models import Contact
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | 
                Q(description__icontains=query) |
                Q(author__icontains=query)
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_term'] = self.request.GET.get('q', '')
        return context
    

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product' : product})

@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:  
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all().order_by('-date')
    contacts = Contact.objects.filter(email=request.user.email).order_by('-created_at')

    context = {
        'form': form,
        'orders': orders,
        'contacts': contacts,
        'on_profile_page': True
    }
    return render(request, 'profiles/profile.html', context)
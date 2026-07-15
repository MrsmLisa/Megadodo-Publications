
from PIL.ImtImagePlugin import field
from django import forms
from .models import Order
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number', 
                'country', 'postcode', 'town_or_city', 
                'street_address1', 'street_address2')
        widgets = {
            'country': CountrySelectWidget(attrs={
                'class': 'form-control mb-3',
                'aria-label': 'Country',})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field in placeholders:
                placeholder = f'{placeholders[field]} *' if self.fields[field].required else placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control mb-3'
            self.fields[field].label = False
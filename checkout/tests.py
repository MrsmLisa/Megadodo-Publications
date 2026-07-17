from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product, Category
from checkout.models import Order, OrderLineItem
from profiles.models import UserProfile


class CheckoutViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.category = Category.objects.create(name='Books')
        self.product = Product.objects.create(
            name='Test Product',
            description='Test description',
            price=9.99,
            sku='TEST001',
            category=self.category,
        )

    def test_checkout_redirects_if_bag_empty(self):
        """Test that checkout redirects if bag is empty"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('product_list'))

    def test_checkout_loads_with_items_in_bag(self):
        """Test that checkout loads when bag has items"""
        self.client.login(username='testuser', password='testpass123')
        session = self.client.session
        session['bag'] = {str(self.product.pk): 1}
        session.save()
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)

    def test_checkout_requires_login(self):
        """Test that checkout redirects if not logged in"""
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)


class OrderModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_order_number_generated(self):
        """Test that order number is generated on save"""
        order = Order.objects.create(
            full_name='Test User',
            email='test@test.com',
            phone_number='12345678',
            street_address1='Test Street',)

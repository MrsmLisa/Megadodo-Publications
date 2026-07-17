# Test code from Claude AI
from django.test import TestCase
from django.urls import reverse
from products.models import Product, Category


class BagViewTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Books')
        self.product = Product.objects.create(
            name='Test Product',
            description='Test description',
            price=9.99,
            sku='TEST001',
            category=self.category,
        )

    def test_bag_page_loads(self):
        """Test that the bag page returns 200"""
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)

    def test_add_to_bag(self):
        """Test adding a product to the bag"""
        response = self.client.post(
            reverse('add_to_bag', args=[self.product.pk]),
            {'quantity': 1, 'redirect_url': '/bag/'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn(
            str(self.product.pk), self.client.session['bag']
        )

    def test_remove_from_bag(self):
        """Test removing a product from the bag"""
        self.client.post(
            reverse('add_to_bag', args=[self.product.pk]),
            {'quantity': 1, 'redirect_url': '/bag/'}
        )
        response = self.client.post(
            reverse('remove_from_bag', args=[self.product.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(
            str(self.product.pk), self.client.session.get('bag', {})
        )
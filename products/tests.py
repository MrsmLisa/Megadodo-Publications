# Test code from Claude AI
from django.test import TestCase
from django.urls import reverse
from .models import Product, Category


class ProductModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Books')
        self.product = Product.objects.create(
            name='Test Product',
            description='Test description',
            price=9.99,
            sku='TEST001',
            category=self.category,
        )

    def test_product_str(self):
        """Test product string representation"""
        self.assertEqual(str(self.product), 'Test Product')

    def test_product_list_loads(self):
        """Test that the product list page returns 200"""
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_loads(self):
        """Test that the product detail page returns 200"""
        response = self.client.get(
            reverse('product_detail', args=[self.product.pk])
        )
        self.assertEqual(response.status_code, 200)

    def test_product_search(self):
        """Test that search returns correct results"""
        response = self.client.get(
            reverse('product_list'), {'q': 'Test'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')
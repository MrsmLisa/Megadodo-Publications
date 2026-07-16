from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image', null=True, blank=True)
    category = models.ForeignKey
    (Category, on_delete=models.CASCADE, related_name='books')
    sku = models.CharField(max_length=50, unique=True)

    def product_url(self):
        return reverse('product_detail', kwargs={'pk': str(self.id)})

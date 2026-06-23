from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
     title = models.CharField(max_length=200)
     author = models.CharField(max_length=100)
     description = models.TextField()
     price = models.DecimalField(max_digits=6, decimal_places=2)
     cover_image = models.ImageField(upload_to='book_covers/')
     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
     sku = models.CharField(max_length=50, unique=True)
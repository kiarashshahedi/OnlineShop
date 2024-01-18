from django.db import models
from myshop import settings


class Category(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True, default=1)  # Set the default value here
    image = models.ImageField(upload_to='product_images/', default='\myshop\staticfiles\admin\img/image.jpg')
    inventory = models.PositiveIntegerField(default=0)
    average_rating = models.FloatField(default=0.0)
    total_ratings = models.IntegerField(default=0)


    def __str__(self):
        return self.name

    def __str__(self):
        return self.name
#----------------------------------------------------------
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
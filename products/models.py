from django.db import models
from myshop import settings
import datetime
from custom_loggin.models import MyUser

#Products Category
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

#All Products
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=3)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/')
    inventory = models.PositiveIntegerField(default=0)
    average_rating = models.FloatField(default=0.0)
    total_ratings = models.IntegerField(default=0)
    # adding sale 
    in_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=9, decimal_places=3)


    def __str__(self):
        return self.name

#the rate of the product
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


#Customers Order
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='customer_orders', related_query_name='customer_order')  # Add related_name and related_query_name
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
    

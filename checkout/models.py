from django.db import models
from cart.models import Cart

class Order(models.Model):
    user = models.ForeignKey('custom_loggin.MyUser', on_delete=models.CASCADE)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

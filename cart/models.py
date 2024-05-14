from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
# Create your models here.



class CartItem(models.Model):

    """
    Create for rest_cart
    """

    cart = models.ForeignKey('Cart',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10,decimal_places=2)


class Cart(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
from django.db import models
from django.utils import timezone
from shop.models import Product
# Create your models here.

class Order(models.Model):
    CITY_LIST = [
        ('a','New York'),
        ('b','Los Angles'),
        ('c','Texas'),
        ('d','San Francisco'),
    ]
    first_name = models.CharField(max_length=255,verbose_name= 'First Name')
    last_name = models.CharField(max_length=255,verbose_name='Last Name')
    email = models.EmailField(verbose_name='E-mail')
    city = models.CharField(max_length=255,choices=CITY_LIST,default='New York',verbose_name='City')
    address = models.TextField(verbose_name='Address')
    postal_code = models.PositiveBigIntegerField(verbose_name='Postal-Code')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order{self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity





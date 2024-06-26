from decimal import Decimal
from django.conf import settings
from shop.models import Product
from django.http import HttpRequest

class Cart:
    def __init__(self,request):
        '''initialize'''
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Save empty cart in session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self,product,quantity=1,update_quantity=False):
        """
        add products or update quantity product
        """
        product_id=str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0,'price':str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity

        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # updated the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Mark the session as a modified to make sure it is saved
        self.session.modified = True

    def remove(self,product):
        """
        remove product from cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        # iterate over the items inthe cart and get the products from the datebase
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            price = Decimal(item['price'])
            quantity = int(item['quantity'])
            item['total_price'] = price * quantity
            yield item

    def __len__(self):
        # Count all items inthe cart
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        total_price= sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())
        return total_price

    def clear(self):
        # Remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified=True

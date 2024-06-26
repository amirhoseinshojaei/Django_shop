from django.shortcuts import render,redirect,get_object_or_404
from shop.models import Product
from .forms import CartAddProductForm
from .cart import Cart
from django.views.decorators.http import require_POST
# Create your views here.

@require_POST
def cart_add(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity = cd['quantity'],
                 update_quantity=cd['update'])

    return redirect("cart:cart_detail")


def cart_remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    """ When using for in, it will start iterating and call `__iter__`"""
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={
                'quantity':item['quantity'],
                'update':True
            }
        )
    return render(request,'cart/detail.html',{'cart':cart})
from django.shortcuts import render,redirect
from cart.cart import Cart
from .models import OrderItem
from .forms import CreateOrderForm
from .task import order_create
from django.http import HttpRequest
# Create your views here.

def order_create(request):

    cart = Cart(request)
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order = order,
                                         product = item['product'],
                                         price = item['price'],
                                         quantity = item['quantity'])

            # clear the cart
            cart.clear()
            order_create(order.id)
            request.session['order_id'] = order.id
            # redirect to payment
            return redirect('payment:process')

    else:
        form = CreateOrderForm()

    return render(request,'orders/order/create.html',{'cart':cart,'form':form})
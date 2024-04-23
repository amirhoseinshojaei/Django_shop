from django.shortcuts import render,get_object_or_404
from .models import Product,Category
from cart.forms import CartAddProductForm
# Create your views here.

def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category = category,available=True)
    context ={
        'category':category,
        'categories':categories,
        'products':products
    }
    return render(request,'shop/products/list.html',context)

def product_detail(request,product_id,slug):
    product = get_object_or_404(Product,id=product_id,slug=slug,available=True)
    category = Category.objects.filter(products=product)
    form = CartAddProductForm()
    return render(request,'shop/products/detail.html',{'product':product,'category':category,
                                                       'form':form})


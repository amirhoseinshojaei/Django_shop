from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('shop/products/',views.product_list,name='products'),
    path('<slug:category_slug>/',views.product_list,name='products_by_category'),
    path('<int:product_id>/<slug:slug>/',views.product_detail,name='product_detail'),
]
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('cart/',include('cart.urls',namespace='cart')),
    path('orders/',include('order.urls',namespace='order')),
    path('payment/',include('payment.urls',namespace='payment')),
    path('paypal/',include('paypal.standard.ipn.urls')),
    path('',include('shop.urls',namespace='shop')),
    path('rest_shop/',include('rest_shop.urls',namespace='rest_shop')),
    path('rest_order/',include('rest_order.urls',namespace='rest_order')),
    path('rest_cart/',include('rest_cart.urls',namespace='rest_cart')),
]

urlpatterns+= static (settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
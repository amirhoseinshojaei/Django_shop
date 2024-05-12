from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .serializers import CartSerializer
from cart.cart import Cart
# Create your views here.

class CartViewset(viewsets.ViewSet):

    def list(self,request):

        cart = Cart(request)
        serializer = CartSerializer(cart)
        permissions = (IsAdminUser)

        return Response(serializer.data)

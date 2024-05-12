from django.shortcuts import render
from order.models import Order,OrderItem
from .serializers import OrderSerializer,OrderItemSerializer
from .permissions import IsSuperUserOrStaff
from rest_framework import viewsets
# Create your views here.

class OrderViewset(viewsets.ModelViewSet):

    queryset= Order.objects.all().order_by('-created_at')
    serializer_class= OrderSerializer
    permission_classes= (IsSuperUserOrStaff,)


class OrderPaidViewset(viewsets.ModelViewSet):

    queryset= Order.objects.filter(paid=True)
    serializer_class = OrderSerializer
    permission_classes = (IsSuperUserOrStaff,)


class OrderItemViewset(viewsets.ModelViewSet):

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsSuperUserOrStaff,)


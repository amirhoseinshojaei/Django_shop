from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer,ProductSerializer
from .permissions import IsUperUserOrStaff
from shop.models import Category,Product
from rest_framework.permissions import IsAdminUser
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsUperUserOrStaff,)

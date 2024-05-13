from rest_framework import serializers
from cart.models import CartItem,Cart
from rest_shop.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:

        model = CartItem
        fields = [
            'id','product',
            'quantity','price',
            'total_price'
        ]
        
        read_only_fields = ['id','total_price']


class CartSerializer(serializers.Serializer):

    items = CartItemSerializer(many=True,read_only=True)

    class Meta:

        model = Cart
        fields = [
            'id', 'user', 'items', 'total_items', 'total_price'
        ]

        read_only_fields = ['id', 'user', 'total_items', 'total_price']
from rest_framework import serializers


class CartItemSerializer(serializers.Serializer):

    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10,decimal_places=2)
    total_price = serializers.DecimalField(max_digits=10,decimal_places=2)


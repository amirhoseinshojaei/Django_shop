from rest_framework import serializers
from order.models import Order,OrderItem

class OrderSerializer(serializers.ModelSerializer):

    total_cost = serializers.SerializerMethodField()

    class Meta:
        
        model = Order
        fields = [
            'first_name','last_name',
            'email','city',
            'address','postal_code',
            'created_at','updated_at','paid'
        ]

        def get_total_cost(self,obj):
            return sum(item.get_cost() for item in obj.items.all())
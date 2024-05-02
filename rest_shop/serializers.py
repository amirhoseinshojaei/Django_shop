from rest_framework import serializers
from shop.models import Category,Product

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']




class ProductSerializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(read_only=True)
    category = CategorySerializer(many = False)

    class Meta:
        model = Product
        fields = ['id',
            'name','slug',
            'category','description',
            'image','publish_at',
            'updated_at','stock',
            'price','available'
        ]
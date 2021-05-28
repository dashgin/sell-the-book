from rest_framework import serializers

from accounts.models import CustomUser
from api.accounts.serializers import UserDetailsSerializer
from products.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    owner = UserDetailsSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'owner', 'title', 'slug', 'category', 'author', 'description', 'image', 'price',
            'amount', 'phone_number', 'additional_contact', 'created_at', 'featured'
        ]
        read_only_fields = ['featured', 'created_at']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['category'] = CategorySerializer(instance.category).data
        return response

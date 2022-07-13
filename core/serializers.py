from rest_framework import serializers
from django_filters import rest_framework as filters
from core.models import Products, Category


# class ProductFilter(filters.FilterSet):
#     min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
#     max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
#
#     class Meta:
#         model = Products
#         fields = ('category', 'in_stock')
#

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'price', 'description', 'image', 'category')


# class ProductDetailCreateUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Products
#         fields = ('id', 'name', 'price', 'description', 'image')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # вытаскивает все поля которые есть

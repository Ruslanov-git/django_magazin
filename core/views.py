from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Products, Category
from core.serializers import ProductSerializer, CategorySerializer


class ProductView(ModelViewSet):
    queryset = Products.objects.all().order_by('-id')   # order_by сортирует показ с конца
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['name', 'description']
    ordering_fields = ['id', 'price']

    # def create(self, request, *args, **kwargs):
    #     print(request.data)


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



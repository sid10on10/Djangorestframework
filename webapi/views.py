from django.shortcuts import render
from rest_framework import viewsets
from .models import Transaction, Product
from .serializers import TransactionSerializer, ProductSerializer


class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
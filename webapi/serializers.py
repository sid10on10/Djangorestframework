from rest_framework import serializers
from .models import Transaction, Product

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id','product_id','transaction_amount','transaction_datetime')
        
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','product_name','productManufacturingCity')
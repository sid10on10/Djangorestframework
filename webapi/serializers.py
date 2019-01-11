from rest_framework import serializers
from .models import Transaction, Product

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id','product_id','transaction_Amount','transaction_DateTime')
        
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','product_name','productManufacturingCity')
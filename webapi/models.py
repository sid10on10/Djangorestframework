from django.db import models

# Create your models here.

class Transaction(models.Model):
    product_id = models.CharField(max_length=120, null=True, blank=True)
    transaction_Amount = models.CharField(max_length=120, null=True, blank=True)
    transaction_DateTime = models.DateTimeField()
    
    def __str__(self):
        return self.product_id
    
class Product(models.Model):
    product_name = models.CharField(max_length=120, null=True, blank=True)
    productManufacturingCity = models.CharField(max_length=120, null=True, blank=True)
    
    def __str__(self):
        return self.product_name
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('transaction', views.TransactionView)
router.register('product', views.ProductView)



urlpatterns = [
    path('', include(router.urls)),
    
]

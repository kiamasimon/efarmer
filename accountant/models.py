from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Accountant(get_user_model()):
    location = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Accountant'


class Admin_User(get_user_model()):
    location = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Admin'


class Stock(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Stock'


class Product(models.Model):
    name = models.CharField(max_length=250)
    number_of_units = models.IntegerField()
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    buying_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'


class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.IntegerField()


class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    units_sold = models.IntegerField()
    price_per_unit = models.IntegerField()
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Sale'
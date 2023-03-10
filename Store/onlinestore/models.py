from django.db import models
from django.contrib.auth.models import User

from multiselectfield import MultiSelectField


class Customer(models.Model):
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE,
                                related_name='customer',
                                null=True,
                                blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    COLOR = [
        ('BLACK', 'Тёмный'),
        ('WHITE', 'Светлый'),
        ('RED', 'Красный'),
        ('BLUE', 'Голубой/Синий'),
        ('GREEN', 'Зелёный'),
    ]
    SIZE = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    ]
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    colors = models.CharField(default='BLACK',
                              max_length=20,
                              choices=COLOR)
    sizes = MultiSelectField(default='XS',
                             max_length=10,
                             choices=SIZE)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)
    data_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True)
    order = models.ForeignKey(Order,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)
    quantity = models.IntegerField(default=0,
                                   blank=True,
                                   null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class ShippingAdress(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)
    order = models.ForeignKey(Order,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)
    state = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    adress = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (self.city, self.adress)

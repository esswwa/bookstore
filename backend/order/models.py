import uuid
from django.db import models

from account.models import User
from basket.models import Basket
from book.models import Book


class Address(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    text = models.TextField(blank=True, null=True)


class Order(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    basket = models.ForeignKey(Basket, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.TextField(blank=True, null=False)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    all_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_order = models.DateTimeField(auto_now_add=True)
    date_delivered = models.DateTimeField(null=True, blank=True)
    date_of_receiving = models.DateTimeField(null=True, blank=True)
    date_order_renewal_end_date = models.DateTimeField(null=True, blank=True)


class OrderHelper(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    all_price = models.DecimalField(max_digits=10, decimal_places=2)
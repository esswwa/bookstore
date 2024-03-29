import uuid
from django.db import models

from account.models import User
from basket.models import Basket


class Address(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    text = models.TextField(blank=True, null=True)


class Order(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    basket = models.ForeignKey(Basket, on_delete=models.DO_NOTHING)
    date_order = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.TextField(blank=True, null=False)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    date_delivered = models.DateTimeField(null=True, blank=True)
    date_of_receiving = models.DateTimeField(null=True, blank=True)
    all_price = models.DecimalField(max_digits=10, decimal_places=2)

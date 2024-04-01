import uuid
from django.db import models

from account.models import User
from book.models import Book


class Basket(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class BasketAdditional(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    all_price = models.DecimalField(max_digits=10, decimal_places=2)




import uuid
from django.db import models

from account.models import User
from book.models import Book


class Review(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    review = models.TextField(blank=True, null=True)
    rating = models.FloatField(default=0)
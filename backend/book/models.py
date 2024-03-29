import uuid
from django.db import models


class Genre(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    text = models.TextField(blank=True, null=True)


class AdditionalGenre(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    text_additional = models.TextField(blank=True, null=True)
    text_genre = models.ForeignKey(Genre,on_delete=models.DO_NOTHING)


class Published(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    text = models.TextField(blank=True, null=True)


class Author(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    text = models.TextField(blank=True, null=True)


class Book(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    description = models.TextField(blank=True, null=False)
    status = models.TextField(blank=True, null=False)
    name = models.TextField(blank=True, null=False)
    type_cover = models.TextField(blank=True, null=True)
    date_of_create = models.IntegerField(default=0, null=True)
    isbn = models.TextField(blank=True, null=False)
    count_of_pages = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    age_restrictions = models.TextField(blank=True, null=True)
    weight = models.IntegerField(default=0)
    cost_per_one = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.TextField(blank=True, null=True)
    additional_genre = models.ForeignKey(AdditionalGenre, on_delete=models.DO_NOTHING)
    publishing_house = models.ForeignKey(Published, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
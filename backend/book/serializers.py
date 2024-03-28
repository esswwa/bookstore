from rest_framework import serializers

from account.serializers import UserSerializer

from .models import Book



class BookSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Book
        fields = ('id', 'description', 'status', 'name', 'type_cover', 'date_of_create', 'isbn', 'count_of_pages', 'rating', 'age_restrictions', 'weight', 'cost_per_one', 'size', 'additional_genre', 'publishing_house', 'author')
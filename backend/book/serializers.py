from rest_framework import serializers

from account.serializers import UserSerializer

from .models import Book, Author, Genre, AdditionalGenre, Published


class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Published
        fields = ('id', 'text')
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'text')
class AdditionalGenreSerializer(serializers.ModelSerializer):
    text_genre = GenreSerializer()
    class Meta:
        model = AdditionalGenre
        fields = ('id', 'text_additional', 'text_genre')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'text')
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    additional_genre = AdditionalGenreSerializer()
    publishing_house = PublishSerializer()
    class Meta:
        model = Book
        fields = ('id', 'description', 'status', 'name', 'type_cover', 'date_of_create', 'isbn', 'count_of_pages', 'rating', 'age_restrictions', 'weight', 'cost_per_one', 'size', 'additional_genre', 'publishing_house', 'author')


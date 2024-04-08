from rest_framework import serializers

from account.serializers import UserSerializer

from book.serializers import BookSerializer

from review.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    user = UserSerializer()
    class Meta:
        model = Review
        fields = ('id', 'date_review', 'user', 'book', 'review', 'rating')


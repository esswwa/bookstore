from rest_framework import serializers

from account.serializers import UserSerializer

from .models import Basket, BasketAdditional
from book.serializers import BookSerializer


class BasketSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Basket
        fields = ('id', 'user')


class BasketAdditionalSerializer(serializers.ModelSerializer):
   basket = BasketSerializer()
   book = BookSerializer()
   class Meta:
        model = BasketAdditional
        fields = ('id', 'basket', 'book', 'count', 'all_price')

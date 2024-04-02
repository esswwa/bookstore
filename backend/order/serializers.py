from rest_framework import serializers

from account.serializers import UserSerializer
from basket.serializers import BasketSerializer

from .models import Order, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'text')
class OrderSerializer(serializers.ModelSerializer):
    basket = BasketSerializer()
    address = AddressSerializer()
    user = UserSerializer()
    class Meta:
        model = Order
        fields = ('id', 'basket', 'date_order', 'user', 'status', 'address', 'date_delivered', 'date_of_receiving', 'all_price')


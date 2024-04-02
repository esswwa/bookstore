import time

from django.db.models import Q
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import JsonResponse
from django.core import serializers
from account.models import User
from favourite.models import Favourite
from basket.models import BasketAdditional
from account.serializers import (UserSerializer)
from rest_framework.response import Response

from .models import Order, Address
from book.models import Book
import logging
from django.core.serializers import serialize
from book.serializers import BookSerializer, AuthorSerializer

from .serializers import OrderSerializer, AddressSerializer
#
# @api_view(['POST'])
# def get_order(request):
# 	basket = Basket
# 	for i in Basket.objects.all():
# 		if i.user.id == request.user.id:
# 			basket = i
# 	basket_additionals = BasketAdditional.objects.filter(basket=basket.id)
# 	all_price = 0
# 	for price in basket_additionals.values_list('all_price', flat=True):
# 		all_price += price
#
# 	book_ids = [book_id.book_id for book_id in basket_additionals]
# 	book_ids = [int(book_id) for book_id in book_ids]
# 	# Получаем книги, соответствующие этим book_id
# 	books = Book.objects.filter(id__in=book_ids)
# 	serializer = BookSerializer(books, many=True)
# 	serializer_basket = BasketSerializer(basket, many=False)
# 	serializer_basket_additional = BasketAdditionalSerializer(basket_additionals, many=True)
#
# 	return JsonResponse({"books": serializer.data, "basket": serializer_basket.data, "basket_additionals": serializer_basket_additional.data, 'all_price': all_price})


@api_view(['GET'])
def get_address(request):

	address = Address.objects.all()
	serializer = AddressSerializer(address, many=True)

	return JsonResponse({"address": serializer.data})



@api_view(['POST'])
def add_order(request):
	data = request.data
	basket_additionals = data['basket_additionals']
	user_id = data['user']
	all_price = data['all_price']
	user = User.objects.get(id=user_id)
	address = Address.objects.get(id=data['selected_item'])

	basket_additionals = BasketAdditional.objects.filter(id=basket_additionals).first()
	print(basket_additionals)
	if basket_additionals:
		order = Order.objects.create(basket=basket_additionals.basket, user=user, status='Оформлен', address=address,all_price=all_price)
		if order:
			basket_additionals = BasketAdditional.objects.filter(basket=basket_additionals.basket)
			basket_additionals.delete()
			last_order = Order.objects.filter(user=user).order_by('-id').first()
			last_order.delete()
			order.save()

			return Response({'message': 'Order added successfully'}, status=status.HTTP_200_OK)
		else:
			return Response({'message': 'Order is not addes'}, status=status.HTTP_400_BAD_REQUEST)
	else:
		return JsonResponse({'message': 'Error basket is empty'}, status=status.HTTP_400_BAD_REQUEST)

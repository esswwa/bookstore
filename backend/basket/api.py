from django.db.models import Q
from django.http import JsonResponse
import uuid

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import JsonResponse
from django.core import serializers
from account.models import User
from favourite.models import Favourite
from account.serializers import (UserSerializer)
from rest_framework.response import Response

from .models import Basket, BasketAdditional
from book.models import Book
import logging
from django.core.serializers import serialize
from book.serializers import BookSerializer, AuthorSerializer

from .serializers import BasketSerializer, BasketAdditionalSerializer


@api_view(['POST'])
def get_basket(request):
	basket = Basket
	for i in Basket.objects.all():
		if i.user.id == request.user.id:
			basket = i
	basket_additionals = BasketAdditional.objects.filter(basket=basket.id)
	all_price = 0
	for price in basket_additionals.values_list('all_price', flat=True):
		all_price += price

	book_ids = [book_id.book_id for book_id in basket_additionals]
	book_ids = [int(book_id) for book_id in book_ids]
	# Получаем книги, соответствующие этим book_id
	books = Book.objects.filter(id__in=book_ids)
	serializer = BookSerializer(books, many=True)
	serializer_basket = BasketSerializer(basket, many=False)
	serializer_basket_additional = BasketAdditionalSerializer(basket_additionals, many=True)

	return JsonResponse({"books": serializer.data, "basket": serializer_basket.data, "basket_additionals": serializer_basket_additional.data, 'all_price': all_price})



# @api_view(['POST'])
# def add_to_basket(request):
# 	data = request.data
# 	book_id = data['book']
# 	user_id = data['user']
# 	basket = Basket
# 	basket_additional = BasketAdditional
# 	book = Book
#
# 	for i in Basket.objects.all():
# 		if i.user.id == user_id:
# 			basket = i
#
# 	for i in BasketAdditional.objects.all():
# 		if i.basket.id == basket.id and i.book.id == book_id:
# 			basket_additional = i
#
# 	for i in Book.objects.all():
# 		if i.id == book_id:
# 			book = i
#
# 	if basket_additional:
# 		print(basket_additional.id)
# 		count_value = getattr(basket_additional, 'count')
# 		print(count_value)
# 		basket_additional.count = int(count_value) + 1
#
# 		all_price = book.cost_per_one * basket_additional.count
# 		if all_price is None:
# 			all_price = 0
#
# 		if book.cost_per_one is not None:
#
# 			basket_additional.all_price = all_price
#
# 			print(basket_additional.count)
# 			print(book.cost_per_one)
# 			print(all_price)
# 			print(basket_additional.all_price)
# 			basket_additional.save()
# 			return Response({'message': 'Basket added successfully'}, status=status.HTTP_200_OK)
# 		else:
# 			return Response({'message': 'Book cost is not set'}, status=status.HTTP_400_BAD_REQUEST)
# 	else:
# 		return Response({'message': 'Basket not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_to_basket(request):
	data = request.data
	book_id = data['book']
	user_id = data['user']
	basket = Basket.objects.get(id=user_id)

	basket_additional = BasketAdditional.objects.get(basket=basket.id, book=book_id)

	book = Book.objects.get(id=book_id)

	if basket_additional:
		count_value = getattr(basket_additional, 'count')
		basket_additional.count = int(count_value) + 1

		all_price = book.cost_per_one * basket_additional.count
		if all_price is None:
			all_price = 0

		if book.cost_per_one is not None:

			basket_additional.all_price = all_price
			basket_additional.save()
			return Response({'message': 'Basket added successfully'}, status=status.HTTP_200_OK)
		else:
			return Response({'message': 'Book cost is not set'}, status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response({'message': 'Basket not found'}, status=status.HTTP_404_NOT_FOUND)


#
# @api_view(['POST'])
# def delete_basket(request):
#     data = request.data
#     book_id = data['book']
#     user_id = data['user']
#
#
#     favourite = Favourite.objects.filter(book_id=book_id, user_id=user_id).first()
#     print(user_id)
#     if favourite:
#         favourite.delete()
#         return Response({'message': 'Favourite deleted successfully'}, status=status.HTTP_200_OK)
#     else:
#         return Response({'message': 'Favourite not found'}, status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['POST'])
# def delete_one_more(request):
#     data = request.data
#     book_id = data['book']
#     user_id = data['user']
#
#
#     favourite = Favourite.objects.filter(book_id=book_id, user_id=user_id).first()
#     print(user_id)
#     if favourite:
#         favourite.delete()
#         return Response({'message': 'Favourite deleted successfully'}, status=status.HTTP_200_OK)
#     else:
#         return Response({'message': 'Favourite not found'}, status=status.HTTP_404_NOT_FOUND)
#

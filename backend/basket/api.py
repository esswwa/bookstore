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
	# for i in Basket.objects.all():
	# 	if i.user.id == request.user.id:
	# 		basket = i
	user = User.objects.get(id=request.data['user'])
	basket = Basket.objects.get(id=user.id)
	basket_additionals = BasketAdditional.objects.filter(basket=basket)
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

@api_view(['POST'])
def add_to_basket(request):
	data = request.data
	book_id = data['book']
	user_id = data['user']
	basket = Basket.objects.get(id=user_id)

	basket_additional = BasketAdditional.objects.filter(basket=basket.id, book=book_id).first()

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
		basket_additional1 = BasketAdditional.objects.create(basket=basket, book=book, count=1, all_price=book.cost_per_one)
		message = 'success'

		# Удаляем последний элемент из favorite
		if BasketAdditional.objects.filter(basket=basket.id, book=book_id).count() > 1:
			last_basket = BasketAdditional.objects.filter(basket=basket.id, book=book_id).order_by('-id').first()
			last_basket.delete()

			# Сохраняем изменения
			basket_additional1.save()

		return JsonResponse({'message': message, "basket_additional": serializers.serialize('json', [basket_additional1, ])})

@api_view(['POST'])
def delete_one_more(request):
	data = request.data
	book_id = data['book']
	user_id = data['user']
	basket = Basket.objects.get(id=user_id)
	book = Book.objects.get(id=book_id)


	basket_additional = BasketAdditional.objects.filter(basket=basket.id, book=book.id).first()

	if basket_additional:
		if basket_additional.count >= 2:
			basket_additional.count -= 1
			basket_additional.all_price = book.cost_per_one * basket_additional.count
			basket_additional.save()
			return Response({'message': 'Basket_additional count - 1 successfully'}, status=status.HTTP_200_OK)
		else:
			basket_additional.delete()
			return Response({'message': 'Basket_additional deleted successfully'}, status=status.HTTP_200_OK)
	else:
		return Response({'message': 'Basket_additional not deleted'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def delete_basket(request):
	data = request.data
	book_id = data['book']
	user_id = data['user']
	basket = Basket.objects.get(id=user_id)
	book = Book.objects.get(id=book_id)

	basket_additional = BasketAdditional.objects.filter(basket=basket.id, book=book.id).first()

	if basket_additional:
		basket_additional.delete()
		return Response({'message': 'Basket_additional deleted successfully'}, status=status.HTTP_200_OK)
	else:
		return Response({'message': 'Basket_additional not deleted'}, status=status.HTTP_404_NOT_FOUND)



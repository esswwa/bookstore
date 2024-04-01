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
	basket_ids = [fav for fav in basket_additionals]
	# Преобразуем book_ids в список числовых значений
	book_ids = [book_id.book for book_id in basket_ids]
	book_ids = [int(book_id) for book_id in book_ids]


	# Получаем книги, соответствующие этим book_id
	books = Book.objects.filter(id__in=book_ids)

	serializer = BookSerializer(books, many=True)
	serializer_basket = BasketSerializer(basket, many=False)
	serializer_basket_additional = BasketAdditionalSerializer(basket_additionals, many=True)

	return JsonResponse({"books": serializer.data, "basket": serializer_basket.data, "basket_additionals": serializer_basket_additional.data})



@api_view(['POST'])
def add_to_basket(request):
    data = request.data
    book_id = data['book_id']
    user_id = data['user_id']
    message = 'error'

    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=user_id)

    if book and user:
        if Favourite.objects.filter(book_id=book_id, user_id=user_id).first() is None:
            favourite = Favourite.objects.create(book_id=book.id, user_id=user.id)
            message = 'success'

            # Удаляем последний элемент из favorite
            if Favourite.objects.filter(user_id=user.id).count() > 1:
                last_favourite = Favourite.objects.filter(user_id=user.id).order_by('-id').first()
                last_favourite.delete()

                # Сохраняем изменения
                favourite.save()

            return JsonResponse({'message': message, "favourite": serializers.serialize('json', [favourite,])})

    if message != 'success':
        message = 'error'
        return JsonResponse({'message': message})


@api_view(['POST'])
def delete_basket(request):
    data = request.data
    book_id = data['book']
    user_id = data['user']


    favourite = Favourite.objects.filter(book_id=book_id, user_id=user_id).first()
    print(user_id)
    if favourite:
        favourite.delete()
        return Response({'message': 'Favourite deleted successfully'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Favourite not found'}, status=status.HTTP_404_NOT_FOUND)

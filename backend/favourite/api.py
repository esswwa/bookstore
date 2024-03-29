from django.db.models import Q
from django.http import JsonResponse
import uuid
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import JsonResponse
from django.core import serializers
from account.models import User
from favourite.models import Favourite
from account.serializers import (UserSerializer)

from .models import Favourite
from book.models import Book
import logging
from django.core.serializers import serialize
from book.serializers import BookSerializer, AuthorSerializer

@api_view(['POST'])
def book_favourite(request):
    favourite = Favourite.objects.filter(user_id=request.user)
    book_ids = [fav.book_id for fav in favourite]  # Получаем все book_id из объектов Favourite

    # Преобразуем book_ids в список числовых значений
    book_ids = [int(book_id) for book_id in book_ids]

    # Получаем книги, соответствующие этим book_id
    books = Book.objects.filter(id__in=book_ids)
    serializer = BookSerializer(books, many=True)
    return JsonResponse({"favourites": serializer.data})



@api_view(['POST'])
def add_to_favourite(request):
    data = request.data
    book_id = data['book_id']
    user_id = data['user_id']
    message = 'error'

    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=user_id)

    if book and user:
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
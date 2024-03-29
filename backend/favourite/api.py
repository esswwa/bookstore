from django.db.models import Q
from django.http import JsonResponse
import uuid
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.models import User
from favourite.models import Favourite
from account.serializers import (UserSerializer)

from .models import Favourite
from book.models import Book
import logging
from django.core.serializers import serialize

@api_view(['GET'])
def book_favourite(request):
	return Favourite.objects.all()
    # user_ids = [request.user.id]
    #
    # for user in request.user.friends.all():
    #     user_ids.append(user.id)

    # books = Book.objects.exclude(status="В наличии")

# @api_view(['POST'])
# def add_to_favourite(request):
# 	logging.basicConfig(filename='app.log', level=logging.DEBUG)
# 	data = request.data
# 	book_id = data['book_id']
# 	user_id = data['user_id']
# 	hex_uuid = uuid.uuid4().hex
# 	if(Book.objects.filter(id=book_id).exists() and User.objects.filter(id=user_id).exists()):
# 		favourite = Favourite.objects.create(id=hex_uuid, book_id=book_id, user_id=user_id)
# 		favourite.save()
# 		message = 'success'
# 		print(message)
# 		return JsonResponse({'message': message, "favourite": favourite})
# 	message = 'error'
# 	book_ids = list(Book.objects.filter(id=book_id).values('id'))
# 	book_all = list(Book.objects.all().values('id'))
# 	return JsonResponse({'message': message, "book_id": book_id, "user_id": user_id, "book_id_fact": book_ids, "book_all": book_all})

# @api_view(['POST'])
# def add_to_favourite(request):
# 	data = request.data
# 	book_id = uuid.UUID(data['book_id'])
# 	user_id = uuid.UUID(data['user_id'])
#
# 	first_book = Book.objects.all().first()  # Получаем первую книгу из запроса
# 	if first_book:
# 		book_id = first_book.id  # Получаем идентификатор (id) этой книги
# 		print(type(book_id))  # Выводим идентификатор на экран
#
#
# 	for i in Book.objects.all():
#
# 		if Book.objects.filter(id=book_id).exists() and User.objects.filter(id=user_id).exists():
# 			favourite = Favourite.objects.create(id=uuid.uuid4().hex, book_id=book_id, user_id=user_id)
# 			favourite.save()
# 			message = 'success'
#
#
# 			logging.info('Favourite created successfully')
#
#
# 			return JsonResponse({'message': message, "favourite": favourite})
# 		else:
# 			message = 'error'
#
#
# 			logging.error('Error creating favourite')
# 			book_ids = list(Book.objects.filter(id=book_id).values('id'))
# 			book_all = list(Book.objects.all().values('id'))
#
#
# 			return JsonResponse({'message': message, "book_id": book_id, "user_id": user_id, "book_id_fact": book_ids,
# 							 "book_all": book_all})


# @api_view(['POST'])
# def add_to_favourite(request):
#     data = request.data
#     book_id = data['book_id']
#     user_id = data['user_id']
#     message = 'error'
#
#     book = Book.objects.get(id=book_id)
#     user = User.objects.get(id=user_id)
#
#     if book and user:
#         favourite, created = Favourite.objects.get_or_create(book_id=book.id, user_id=user.id)
#         message = 'success'
#         favourite.save()
#         favourite.pop()
#         favourite.save()
#         return JsonResponse({'message': message, "favourite": serialize('json', [favourite,])})
#
#     if message != 'success':
#         message = 'error'
#         return JsonResponse({'message': message})

from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.core import serializers

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
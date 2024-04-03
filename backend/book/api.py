from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.models import User
from account.serializers import (UserSerializer)

from .models import Book, Genre
from .serializers import BookSerializer, GenreSerializer


@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)

    return JsonResponse({'books': serializer.data}, safe=False)

@api_view(['GET'])
def get_book(request, id):
    books = Book.objects.get(id=id)
    print(books)
    serializer = BookSerializer(books, many=False)

    return JsonResponse({'book': serializer.data}, safe=False)

@api_view(['GET'])
def books_the_best(request):
    # user_ids = [request.user.id]
    #
    # for user in request.user.friends.all():
    #     user_ids.append(user.id)

    # books = Book.objects.exclude(status="В наличии")
    books = Book.objects.filter(status="В наличии")
    # author = books.values('author')
    serializer = BookSerializer(books, many=True)
    # serializer2 = AuthorSerializer(author, many=True)

    return JsonResponse({'books_the_best': serializer.data}, safe=False)

@api_view(['GET'])
def books_new_items(request):
    # user_ids = [request.user.id]
    #
    # for user in request.user.friends.all():
    #     user_ids.append(user.id)

    # books = Book.objects.exclude(status="В наличии")
    books = Book.objects.filter(status="В наличии")
    # author = books.values('author')
    serializer = BookSerializer(books, many=True)
    # serializer2 = AuthorSerializer(author, many=True)

    return JsonResponse({'books_new_items': serializer.data}, safe=False)

@api_view(['GET'])
def books_popular(request):
    # user_ids = [request.user.id]
    #
    # for user in request.user.friends.all():
    #     user_ids.append(user.id)

    # books = Book.objects.exclude(status="В наличии")
    books = Book.objects.filter(status="В наличии")
    # author = books.values('author')
    serializer = BookSerializer(books, many=True)
    # serializer2 = AuthorSerializer(author, many=True)

    return JsonResponse({'books_popular': serializer.data}, safe=False)


@api_view(['GET'])
def get_pagination(request, page):
    books = Book.objects.filter(status="В наличии")

    count = books.count()

    start_index = (page - 1) * 9

    end_index = start_index + 9

    books = books[start_index:end_index]

    serializer = BookSerializer(books, many=True)

    return JsonResponse({'books': serializer.data, 'count': count}, safe=False)


@api_view(['GET'])
def get_genres(request):

    genres = Genre.objects.all()

    serializer = GenreSerializer(genres, many=True).data

    return JsonResponse({'genres': serializer}, safe=False)
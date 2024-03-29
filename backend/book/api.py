from django.db.models import Q
from django.http import JsonResponse
import uuid
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.models import User
from favourite.models import Favourite
from account.serializers import (UserSerializer)


from .forms import BookForm
from .models import Book, Author, Published, AdditionalGenre, Genre
from .serializers import BookSerializer, AuthorSerializer


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


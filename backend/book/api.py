from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.models import User
from account.serializers import (UserSerializer)

from .models import Book, Genre, AdditionalGenre
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
    # можно посмотреть количество рейтинга у книг, сравнить с
    # другими, затем смотреть, чтобы рейтинг был выше 4.6, и можно еще добавить
    # сравнение, чтобы у пользователей было много рецензий и все они были разными
    # и так вывести топ 10 лучших



    books = Book.objects.filter(status="В наличии")
    serializer = BookSerializer(books, many=True)
    return JsonResponse({'books_the_best': serializer.data}, safe=False)

@api_view(['GET'])
def books_new_items(request):
    # можно искать новые книги, которые были выпущены в течении 3-х месяцев
    # но от авторов или издательств, у которых общая сумма рейтинга их книг
    # составляла хороший рейтинг и при этом было по 0 рецензий на данную книгу


    books = Book.objects.filter(status="В наличии")
    serializer = BookSerializer(books, many=True)

    return JsonResponse({'books_new_items': serializer.data}, safe=False)

@api_view(['GET'])
def books_popular(request):
    # можно посмотреть количество рейтинга у книг, сравнить с
    # другими, затем смотреть, чтобы рейтинг был выше 4.6, и можно еще добавить
    # сравнение, чтобы у пользователей было много рецензий и все они были разными
    # и так вывести топ 10 лучших, но все это с фильтром 2024 года
    books = Book.objects.filter(status="В наличии")
    serializer = BookSerializer(books, many=True)
    return JsonResponse({'books_popular': serializer.data}, safe=False)


@api_view(['POST'])
def get_pagination(request, page):
    if request.data['selected_genres']:
        genres = Genre.objects.filter(id__in=request.data['selected_genres'])
        genre_additionals = AdditionalGenre.objects.filter(text_genre_id__in=genres)
        books = Book.objects.filter(status="В наличии", genre__in=genres)
        count = books.count()
        start_index = (page - 1) * 12
        end_index = start_index + 12
        if request.data['sort_order'] != 'Без сортировки':
            books = books.order_by('-'+request.data['sort_order'])
    else:
        books = Book.objects.filter(status="В наличии")
        if request.data['sort_order'] != 'Без сортировки':
            books = books.order_by('-' + request.data['sort_order'])
        count = books.count()
        start_index = (page - 1) * 12
        end_index = start_index + 12

    books = books[start_index:end_index]

    serializer = BookSerializer(books, many=True)

    return JsonResponse({'books': serializer.data, 'count': count}, safe=False)


@api_view(['GET'])
def get_genres(request):

    genres = Genre.objects.all()

    serializer = GenreSerializer(genres, many=True).data

    return JsonResponse({'genres': serializer}, safe=False)
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


    books = Book.objects.filter(status='В наличии')
    books_rating = []
    for book in books:
        if book.rating >= 4.6:
            books_rating.append(book)

    books_rating.sort(key=lambda x: x.rating, reverse=True)
    books_rating.sort(key=lambda x: x.count_rating, reverse=True)
    books_rating = books_rating[:10]
    serializer = BookSerializer(books_rating, many=True)
    return JsonResponse({'books_popular': serializer.data}, safe=False)

@api_view(['GET'])
def books_new_items(request):
    # task
    # можно искать новые книги, которые были выпущены в течении 3-х месяцев
    # но от авторов или издательств, у которых общая сумма рейтинга их книг
    # составляла хороший рейтинг и при этом было по 0 рецензий на данную книгу


    books = Book.objects.filter(status='В наличии', date_of_create=2024)
    books_rating1 = []
    for book in books:
        if book.rating == 0:
            books_rating1.append(book)
    book_checks = []
    for book in books_rating1:
        book_check = Book.objects.filter(author=book.author)
        book_count = book_check.count()
        book_rating = 0
        for book_check_2 in book_check:
            book_rating += book_check_2.rating
        books_rating = book_rating / book_count
        if book_count > 2 and books_rating >= 4.6:
            book_checks.append(book)

    book_checks.sort(key=lambda x: x.rating, reverse=True)
    book_checks.sort(key=lambda x: x.count_rating, reverse=True)
    book_checks = book_checks[:10]
    books_rating1 = books_rating1[:10]
    if book_checks:
        serializer = BookSerializer(book_checks, many=True)
    else:
        serializer = BookSerializer(books_rating1, many=True)

    print(book_checks)
    print(books_rating1)
    return JsonResponse({'books_new_items': serializer.data}, safe=False)

@api_view(['GET'])
def books_popular(request):
    # можно посмотреть количество рейтинга у книг, сравнить с
    # другими, затем смотреть, чтобы рейтинг был выше 4.6, и можно еще добавить
    # сравнение, чтобы у пользователей было много рецензий и все они были разными
    # и так вывести топ 10 лучших, но все это с фильтром 2024 года

    books = Book.objects.filter(status='В наличии', date_of_create=2024)
    books_rating = []
    for book in books:
        if book.rating >= 4.6:
            books_rating.append(book)

    books_rating.sort(key=lambda x: x.rating, reverse=True)
    books_rating = books_rating[:10]
    serializer = BookSerializer(books_rating, many=True)
    return JsonResponse({'books_popular': serializer.data}, safe=False)


@api_view(['POST'])
def get_pagination(request, page):
    print(request.data['searchInput'] )
    if request.data['selected_genres']:
        genres = Genre.objects.filter(id__in=request.data['selected_genres'])
        genre_additionals = AdditionalGenre.objects.filter(text_genre_id__in=genres)
        books = Book.objects.filter(status="В наличии", genre__in=genres)
        count = books.count()
        start_index = (page - 1) * 12
        end_index = start_index + 12
        if request.data['searchInput'] != '':
            books = books.filter(name__contains=request.data['searchInput'])
            count = books.count()
            start_index = (page - 1) * 12
            end_index = start_index + 12
            if request.data['sort_order'] != 'Без сортировки':
                books = books.order_by('-'+request.data['sort_order'])
        else:
            if request.data['sort_order'] != 'Без сортировки':
                books = books.order_by('-'+request.data['sort_order'])
    elif request.data['searchInput'] == '':
        books = Book.objects.filter(status="В наличии")
        if request.data['sort_order'] != 'Без сортировки':
            books = books.order_by('-' + request.data['sort_order'])
        count = books.count()
        start_index = (page - 1) * 12
        end_index = start_index + 12
    else:
        books = Book.objects.filter(status="В наличии", name__contains=request.data['searchInput'])
        count = books.count()
        start_index = (page - 1) * 12
        end_index = start_index + 12
        if request.data['sort_order'] != 'Без сортировки':
            books = books.order_by('-'+request.data['sort_order'])

    books = books[start_index:end_index]

    serializer = BookSerializer(books, many=True)

    return JsonResponse({'books': serializer.data, 'count': count}, safe=False)


@api_view(['GET'])
def get_genres(request):

    genres = Genre.objects.all()

    serializer = GenreSerializer(genres, many=True).data

    return JsonResponse({'genres': serializer}, safe=False)
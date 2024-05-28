from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from account.models import User
from account.serializers import (UserSerializer)
from rest_framework.response import Response

from .models import Book, Genre, AdditionalGenre, Author, ViewedBook, SimilarBook
from .serializers import BookSerializer, GenreSerializer, AuthorSerializer


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

@api_view(['POST'])
def get_pagination_author(request, author, page):
    print(request.data['searchInput'] )
    authors = Author.objects.get(id=author)
    if request.data['selected_genres']:
        genres = Genre.objects.filter(id__in=request.data['selected_genres'])
        genre_additionals = AdditionalGenre.objects.filter(text_genre_id__in=genres)
        books = Book.objects.filter(status="В наличии", author=authors, genre__in=genres)
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
        books = Book.objects.filter(status="В наличии", author=authors)
        if request.data['sort_order'] != 'Без сортировки':
            books = books.order_by('-' + request.data['sort_order'])
        count = books.count()
        start_index = (page - 1) * 12
        end_index = start_index + 12
    else:
        books = Book.objects.filter(status="В наличии", name__contains=request.data['searchInput'], author=authors)
        count = books.count()
        start_index = (page - 1) * 12
        end_index = start_index + 12
        if request.data['sort_order'] != 'Без сортировки':
            books = books.order_by('-'+request.data['sort_order'])

    books = books[start_index:end_index]

    serializer = BookSerializer(books, many=True)

    return JsonResponse({'books': serializer.data, 'count': count}, safe=False)


@api_view(['POST'])
def add_view(request):
    data = request.data
    bookId = data['bookId']
    user_id = data['user']
    user = User.objects.get(id=user_id)
    book = Book.objects.get(id=bookId)
    # viewed_book = ViewedBook.objects.get(book=book, user=user)
    # # if viewed_book:
    # #     return Response({'message': 'Book already viewed'}, status=status.HTTP_200_OK)
    # # else:
    # #     viewed_book = ViewedBook.objects.create(book=book, user=user)
    # #     if viewed_book:
    # #         viewed_book.save()
    # #         return Response({'message': 'Book viewed added'}, status=status.HTTP_200_OK)
    # #     else:
    # #         return JsonResponse({'message': 'Book viewed dont added'}, status=status.HTTP_400_BAD_REQUEST)
    # try:
    #     viewed_book = ViewedBook.objects.get(book=book, user=user)
    #     return Response({'message': 'Book already viewed'}, status=status.HTTP_200_OK)
    # except ViewedBook.DoesNotExist:
    #     viewed_book = ViewedBook.objects.create(book=book, user=user)
    #     if viewed_book:
    #         viewed_book.save()
    #         return Response({'message': 'Book viewed added'}, status=status.HTTP_200_OK)
    #     else:
    #         return JsonResponse({'message': 'Book viewed dont added'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        book = Book.objects.get(id=bookId)
    except Book.DoesNotExist:
        return Response({'message': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    viewed_book, created = ViewedBook.objects.get_or_create(book=book, user=user)

    if not created:
        return Response({'message': 'Book already viewed'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Book viewed added'}, status=status.HTTP_200_OK)



@api_view(['POST'])
def get_viewed_books(request):

    user = User.objects.get(id=request.data['user_id'])
    viewed_books = ViewedBook.objects.filter(user=user)
    print(viewed_books)
    books = [viewed_book.book for viewed_book in viewed_books]
    print(books)
    serializer = BookSerializer(books, many=True).data

    return JsonResponse({'viewedBooks': serializer}, safe=False)

@api_view(['POST'])
def get_similar_books(request):
    book_id = request.data['book_id']
    book = Book.objects.get(id=book_id)
    similar_books = SimilarBook.objects.filter(book_id=book)
    books = Book.objects.filter(id__in=[sb.book_for_similar_id for sb in similar_books])
    serializer = BookSerializer(books, many=True)
    return JsonResponse({'similar_books': serializer.data}, safe=False)

@api_view(['POST'])
def resulting_similar_books(request):


    books = Book.objects.all()







    return JsonResponse({'similar_books': serializer.data}, safe=False)

@api_view(['GET'])
def get_genres(request):

    genres = Genre.objects.all()

    serializer = GenreSerializer(genres, many=True).data

    return JsonResponse({'genres': serializer}, safe=False)

@api_view(['GET'])
def get_author(request, author):

    authors = Author.objects.get(id=author)

    serializer = AuthorSerializer(authors, many=False).data

    return JsonResponse({'author': serializer}, safe=False)
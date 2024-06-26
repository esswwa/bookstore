from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
import pandas as pd
import numpy as np
from account.models import User
from account.serializers import (UserSerializer)
from rest_framework.response import Response

from .models import Book, Genre, AdditionalGenre, Author, ViewedBook, SimilarBook
from .serializers import BookSerializer, GenreSerializer, AuthorSerializer
from review.models import Review


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


def review_to_dict(instance):
    opts = instance._meta
    data = {}
    for f in opts.concrete_fields + opts.many_to_many:
        if f.name in ['id', 'rating', 'book', 'user']:  # Укажите нужные поля
            data[f.name] = f.value_from_object(instance)
    return data


def book_to_dict(instance):
    opts = instance._meta
    data = {}
    for f in opts.concrete_fields + opts.many_to_many:
        if f.name in ['id', 'name', 'rating']:  # Укажите нужные поля
            data[f.name] = f.value_from_object(instance)
    return data
def same_books(book):
    users_vote_film=users_pivot[book]
    similar_with=users_pivot.corrwith(users_vote_film)
    similar_with = pd.DataFrame(similar_with, columns=['correlation'])
    print(similar_with)
    df=similar_with.sort_values('correlation',ascending=False).head(10)
    print(df)
    df_sort=df[df['correlation']>0.8]
    return df_sort

@api_view(['GET'])
def resulting_similar_books(request):
    SimilarBook.objects.all().delete()
    reviews = Review.objects.all()
    data = [review_to_dict(review) for review in reviews]
    df = pd.DataFrame(data)
    new_df = df[df['user'].map(df['user'].value_counts()) > 3]
    users_pivot = new_df.pivot_table(index=["user"], columns=["book"], values="rating")
    users_pivot.fillna(0, inplace=True)
    from sklearn.metrics.pairwise import cosine_similarity
    similarity_score = cosine_similarity(users_pivot.T)
    users_pivot2 = users_pivot.T

    books = Book.objects.all()
    data2 = [book_to_dict(book) for book in books]
    books = pd.DataFrame(data2)

    def recommend(book_name):
        try:
            index = np.where(users_pivot2.index == book_name)[0][0]
        except IndexError:
            return []

        similar_books = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:11]

        data = []

        for i in similar_books:
            item = []
            temp_df = books[books['id'] == users_pivot2.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('id')['id'].values))
            item.extend(list(temp_df.drop_duplicates('id')['name'].values))
            item.extend(list(temp_df.drop_duplicates('id')['rating'].values))

            data.append(item)
        return data
    for i in books['id']:
        data = recommend(i)
        print(data)
        for j in data:
            bookI = Book.objects.get(id=i)
            bookJ = Book.objects.get(id=j[0])
            similar_book, created = SimilarBook.objects.get_or_create(book_id=bookI.id, book_for_similar_id=bookJ.id)
            similar_book.save()
    return Response({'message': 'OK'}, status=status.HTTP_200_OK)



def get_first_user_movies(users_pivot, key):
    return users_pivot.T[key].sort_values(ascending=False).loc[lambda s: s >= 4.5]


def get_choosed_user_movies(users_pivot, key):
    return users_pivot.T[key].sort_values(ascending=False).loc[lambda s: s == 0]


def get_similar_with(users_pivot, userid):
    corr_series = users_pivot.corrwith(users_pivot[userid])
    # Фильтровать серию корреляций, чтобы включать только положительные и не идеальные корреляции
    similar_users = corr_series[(corr_series > 0.45) & (corr_series < 0.99)].to_dict()

    return similar_users


def get_common_values(df1, df2):
    print('huy', df1.columns)
    print('huy2', df2.columns)

    return pd.merge(df1, df2, on='book', how='inner')


@api_view(['POST'])
def personal_recommendation_system(request):
    request_data = request.data
    reviews = Review.objects.all()
    data = [review_to_dict(review) for review in reviews]
    df = pd.DataFrame(data)
    new_df = df[df['user'].map(df['user'].value_counts()) > 3]
    users_pivot = new_df.pivot_table(index=["user"], columns=["book"], values="rating")
    users_pivot.fillna(0, inplace=True)
    similar_with = get_similar_with(users_pivot, int(request_data['user_id']))
    first_key = int(next(iter(similar_with)))
    first_user_movies = pd.DataFrame(data=get_first_user_movies(users_pivot, first_key).index)
    choosed_user_movies = pd.DataFrame(data=get_choosed_user_movies(users_pivot, int(request_data['user_id'])).index)

    common_values = get_common_values(first_user_movies, choosed_user_movies)
    print("gg12312312", common_values['book'])
    book_id = []
    for key, value in common_values['book'].items():
        book_id.append(value)
    print('book_id', book_id)
    if len(book_id) >= 5:
        if len(book_id) > 10:
            book_id = book_id[:10]
        books = Book.objects.filter(id__in=book_id)
        books = BookSerializer(books, many=True).data
        return Response({'message': 'Recommendations completed', 'books': books, 'count_recommendation': len(book_id)}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Recommendation dont exist'}, status=status.HTTP_200_OK)


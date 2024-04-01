from django.urls import path

from . import api


urlpatterns = [
    path('', api.book_list, name='book_list'),
	path('<int:id>/', api.get_book, name='get_book'),
    path('books_the_best/', api.books_the_best, name='books_the_best'),
    path('books_new_items/', api.books_new_items, name='books_new_items'),
    path('get_pagination/<int:page>/', api.get_pagination, name='get_pagination'),
    path('books_popular/', api.books_popular, name='books_popular'),
]
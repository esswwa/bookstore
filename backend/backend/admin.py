from django.contrib import admin
from account.models import User
from basket.models import Basket, BasketAdditional
from book.models import SimilarBook, ViewedBook, Book, Published, AdditionalGenre, Genre
from order.models import Address, Order, OrderHelper
from review.models import Review


admin.site.register(User)
admin.site.register(Basket)
admin.site.register(BasketAdditional)
admin.site.register(SimilarBook)
admin.site.register(ViewedBook)
admin.site.register(Book)
admin.site.register(Published)
admin.site.register(AdditionalGenre)
admin.site.register(Genre)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderHelper)
admin.site.register(Review)
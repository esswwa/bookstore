from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path('', api.book_favourite, name='book_favourite'),
    path('add_to_favourite/', api.add_to_favourite, name='add_to_favourite')

]
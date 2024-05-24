from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
    path('', api.book_favourite, name='book_favourite'),
    path('add_to_favourite/', api.add_to_favourite, name='add_to_favourite'),
    path('delete_favourite/', api.delete_favourite, name='delete_favourite'),
    path('get_count_favourite/', api.get_count_favourite, name='get_count_favourite'),
    path('get_pagination/<int:page>/', api.get_pagination, name='get_pagination')

]
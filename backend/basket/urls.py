from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
	path('', api.get_basket, name='get_basket'),
	path('add_to_basket/', api.add_to_basket, name='add_to_basket'),
	path('delete_basket/', api.delete_basket, name='delete_basket')
]
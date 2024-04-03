from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
	path('', api.get_order, name='get_order'),
	path('get_address/', api.get_address, name='get_address'),
	path('add_order/', api.add_order, name='add_order'),
	path('add_helper_order/', api.add_helper_order, name='add_helper_order'),
	path('get_helper_order/<int:id>/', api.get_helper_order, name='get_helper_order')

]
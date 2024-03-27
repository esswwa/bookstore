from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [

	path('me/', api.me, name='me'),
	path('signup/', api.signup, name='signup'),
	path('signin/', TokenObtainPairView.as_view(), name='token_obtain'),
	path('refresh/', TokenRefreshView.as_view(), name='token_refresh')

]
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api

urlpatterns = [
path('<int:id>/', api.get_review, name='get_review'),
path('add_review/', api.add_review, name='add_review'),
]
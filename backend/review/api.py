import time

from django.db.models import Q
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import JsonResponse
from django.core import serializers
from account.models import User
from favourite.models import Favourite
from basket.models import BasketAdditional
from account.serializers import (UserSerializer)
from rest_framework.response import Response

from .models import Review
from book.models import Book
import logging
from django.core.serializers import serialize
from book.serializers import BookSerializer, AuthorSerializer

from .serializers import ReviewSerializer


@api_view(['GET'])
def get_review(request, id):
	print(id)
	review = Review.objects.filter(book=id)
	review = ReviewSerializer(review, many=True).data
	return JsonResponse({"reviews": review})


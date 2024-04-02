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


@api_view(['POST'])
def get_review(request, id):
	user = request.user
	user = User.objects.get(id=user.id)
	review_check = Review.objects.filter(book=id, user=user).first()
	check = False
	if review_check:
		check = True
	review = Review.objects.filter(book=id)
	review = ReviewSerializer(review, many=True).data
	return JsonResponse({"reviews": review, "check": check, })

@api_view(['POST'])
def add_review(request):
	print(request.data)
	user = request.data['user']
	book = request.data['book']
	user = User.objects.get(id=user)
	book = Book.objects.get(id=book)
	review = Review.objects.filter(book=book, user=user).first()
	if request.data['review'] != '' and int(request.data['rating']) > 0 and int(request.data['rating']) <= 5:
		if review is None:
			review = Review.objects.create(book=book, user=user, rating=request.data['rating'], review=request.data['review'])
			last_review = Review.objects.filter(user=user).order_by('-id').first()
			last_review.delete()
			review.save()
			return Response({'message': 'Order added successfully'}, status=status.HTTP_200_OK)
	else:
		return Response({'message': 'Order is not added'}, status=status.HTTP_400_BAD_REQUEST)

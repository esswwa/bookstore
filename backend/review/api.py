from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from account.models import User
from rest_framework.response import Response

from .models import Review
from book.models import Book

from .serializers import ReviewSerializer
from order.models import Order, OrderHelper


@api_view(['POST'])
def get_review(request, id, page):
	user = request.user
	user = User.objects.get(id=user.id)
	review_check = Review.objects.filter(book=id, user=user).first()
	check_order = Order.objects.filter(user=user.id)
	check_order = OrderHelper.objects.filter(order_id__in=check_order)
	check_order = check_order.filter(book=id).first()
	order_check = False
	if check_order:
		order_check = True
	print(order_check)
	check = False
	if review_check:
		check = True

	review = Review.objects.filter(book=id)
	if review:
		count = review.count()
		start_index = (page - 1) * 5
		end_index = start_index + 5

		review = review[start_index:end_index]

		review = ReviewSerializer(review, many=True).data
		return JsonResponse({"reviews": review, "check": check, "checkOrder": order_check, 'count': count})
	else:
		return JsonResponse({'message': 'Reviews doesnt have in db',"reviews": [], "check": False, "checkOrder": order_check})
@api_view(['POST'])
def add_review(request):
	user = request.data['user']
	book = request.data['book']
	user = User.objects.get(id=user)
	book = Book.objects.get(id=book)
	review = Review.objects.filter(book=book, user=user).first()
	rating = 0
	if request.data['review'] != '' and int(request.data['rating']) >= 0 and int(request.data['rating']) <= 5:
		if review is None:
			review = Review.objects.create(book=book, user=user, rating=request.data['rating'], review=request.data['review'])
			last_review = Review.objects.filter(user=user).order_by('-id').first()
			last_review.delete()
			review.save()
			review2 = Review.objects.filter(book=book)
			if review2.count() > 1:
				for i in Review.objects.filter(book=book):
					rating += i.rating
				book.rating = rating / review2.count()
			else:
				book.rating = review.rating
			book.count_rating += 1
			book.save()
			return Response({'message': 'Order added successfully'}, status=status.HTTP_200_OK)
	else:
		return Response({'message': 'Order is not added'}, status=status.HTTP_400_BAD_REQUEST)

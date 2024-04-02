from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from account.models import User
from basket.models import BasketAdditional
from rest_framework.response import Response

from .models import Order, Address

from .serializers import OrderSerializer, AddressSerializer

@api_view(['POST'])
def get_order(request):

	user = request.user

	order_active = Order.objects.filter(Q(user=user) & (Q(status='В пути') | Q(status='Оформлен') | Q(status='В пункте выдачи')))

	order_canceled = Order.objects.filter(user=user, status='Отменен')

	order_archive = Order.objects.filter(user=user, status='Завершен')

	order_active = OrderSerializer(order_active, many=True)
	order_canceled = OrderSerializer(order_canceled, many=True)
	order_archive = OrderSerializer(order_archive, many=True)

	return JsonResponse({"activeOrders": order_active.data, "canceledOrders": order_canceled.data, "archiveOrders": order_archive.data})


@api_view(['GET'])
def get_address(request):

	address = Address.objects.all()
	serializer = AddressSerializer(address, many=True)

	return JsonResponse({"address": serializer.data})



@api_view(['POST'])
def add_order(request):
	data = request.data
	basket_additionals = data['basket_additionals']
	user_id = data['user']
	all_price = data['all_price']
	user = User.objects.get(id=user_id)
	address = Address.objects.get(id=data['selected_item'])

	basket_additionals = BasketAdditional.objects.filter(id=basket_additionals).first()
	print(basket_additionals)
	if basket_additionals:
		order = Order.objects.create(basket=basket_additionals.basket, user=user, status='Оформлен', address=address,all_price=all_price)
		if order:
			basket_additionals = BasketAdditional.objects.filter(basket=basket_additionals.basket)
			basket_additionals.delete()
			last_order = Order.objects.filter(user=user).order_by('-id').first()
			last_order.delete()
			order.save()

			return Response({'message': 'Order added successfully'}, status=status.HTTP_200_OK)
		else:
			return Response({'message': 'Order is not addes'}, status=status.HTTP_400_BAD_REQUEST)
	else:
		return JsonResponse({'message': 'Error basket is empty'}, status=status.HTTP_400_BAD_REQUEST)

from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from account.models import User
from basket.models import BasketAdditional
from rest_framework.response import Response
from django.conf import settings
from .models import Order, Address, OrderHelper

from datetime import timedelta
from django.utils import timezone

from .serializers import OrderSerializer, AddressSerializer, HelperOrderSerializer
from django.core.mail import EmailMultiAlternatives

from book.serializers import BookSerializer

from book.models import Book


@api_view(['POST'])
def get_order(request):

	user = request.user

	order_active = Order.objects.filter(Q(user=user) & (Q(status='В пути') | Q(status='Оформлен') | Q(status='В пункте выдачи')))

	order_all = Order.objects.filter(user=user)

	order_canceled = Order.objects.filter(Q(user=user) & (Q(status='Отменен') | Q(status='Не выкуплен')))

	order_archive = Order.objects.filter(user=user, status='Завершен')

	for order in order_active:
		if order.status == 'В пункте выдачи':
			if order.date_delivered < timezone.now() - timedelta(weeks=2):
				order.status = 'Не выкуплен'
				if order:
					order.save()
	order_active = OrderSerializer(order_active, many=True)
	order_canceled = OrderSerializer(order_canceled, many=True)
	order_archive = OrderSerializer(order_archive, many=True)

	return JsonResponse({"allOrders": order_all.data, "activeOrders": order_active.data, "canceledOrders": order_canceled.data, "archiveOrders": order_archive.data})


@api_view(['POST'])
def admin_orders(request, page):
	status_list = [
		{"id": 1, "text": "Оформлен"},
		{"id": 2, "text": "В пути"},
		{"id": 3, "text": "В пункте выдачи"},
		{"id": 4, "text": "Завершен"},
		{"id": 5, "text": "Отменен"},
		{"id": 6, "text": "Не выкуплен"}
	]
	if request.data['selected_filter']:

		selected_ids = [int(id) for id in request.data['selected_filter']]
		filtered_statuses = [status['text'] for status in status_list if status['id'] in selected_ids]
		orders = Order.objects.filter(status__in=filtered_statuses)

		count = orders.count()
		start_index = (page - 1) * 12
		end_index = start_index + 12
		if request.data['search_input'] != '':
			orders = Order.objects.filter(id__in=request.data['search_input'])
			count = orders.count()
			start_index = (page - 1) * 12
			end_index = start_index + 12
			if request.data['sort_order'] != 'Без сортировки':
				orders = orders.order_by('-' + request.data['sort_order'])
		else:
			if request.data['sort_order'] != 'Без сортировки':
				orders = orders.order_by('-' + request.data['sort_order'])
	elif request.data['search_input'] == '':
		orders = Order.objects.all()
		if request.data['sort_order'] != 'Без сортировки':
			orders = orders.order_by('-' + request.data['sort_order'])
		count = orders.count()
		start_index = (page - 1) * 12
		end_index = start_index + 12
	else:
		orders = Order.objects.filter(id__in=request.data['searchInput'])
		count = orders.count()
		start_index = (page - 1) * 12
		end_index = start_index + 12
		if request.data['sort_order'] != 'Без сортировки':
			orders = orders.order_by('-' + request.data['sort_order'])

	orders = orders[start_index:end_index]

	serializer = OrderSerializer(orders, many=True)


	order_active = Order.objects.filter(status='В пункте выдачи')

	for order in order_active:
		if order.status == 'В пункте выдачи':
			if order.date_delivered < timezone.now() - timedelta(weeks=2):
				order.status = 'Не выкуплен'
				if order:
					order.save()

	return JsonResponse({"orders": serializer.data, 'count': count}, safe=False)



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
	if basket_additionals:
		order = Order.objects.create(basket=basket_additionals.basket, user=user, status='Оформлен', address=address,all_price=all_price)
		if order:
			basket_additionals = BasketAdditional.objects.filter(basket=basket_additionals.basket)
			basket_additionals_list = []
			for basket_additional in basket_additionals:
				basket_additionals_list.append({'book': basket_additional.book.id, 'count': basket_additional.count,
												'all_price': basket_additional.all_price})
			basket_additionals.delete()
			last_order = Order.objects.filter(user=user).order_by('-id').first()
			last_order.delete()
			order.save()
			order = Order.objects.all().order_by('-id')[0]
			print(order)

			order = OrderSerializer(order, many=False).data
			return Response({'message': 'Order added successfully', 'basket_additionals_list': basket_additionals_list, 'order': order, 'address': address.text}, status=status.HTTP_200_OK)
		else:
			return Response({'message': 'Order is not addes'}, status=status.HTTP_400_BAD_REQUEST)
	else:
		return JsonResponse({'message': 'Error basket is empty'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_helper_order(request):
	data = request.data
	basket_additionals_list = data['basket_additionals_list']
	for basket_additional in basket_additionals_list:
		basket_additional['book'] = Book.objects.get(id=basket_additional['book'])
	order = data['order']
	order = Order.objects.get(id=order['id'])
	print(basket_additionals_list)
	for basket_additional in basket_additionals_list:
		order_helper = OrderHelper.objects.create(order=order, book=basket_additional['book'], count=basket_additional['count'], all_price=basket_additional['all_price'])
		if order_helper:
			last_order_helper = OrderHelper.objects.filter(order=order, book=basket_additional['book']).order_by('-id').first()
			last_order_helper.delete()
			order_helper.save()
	return Response({'message': 'Order added successfully'}, status=status.HTTP_200_OK)



@api_view(['POST'])
def get_helper_order(request):
	data = request.data
	order = Order.objects.filter(id=data['order'])
	order_active = OrderHelper.objects.filter(order__in=order)
	order_active = HelperOrderSerializer(order_active, many=True)
	return JsonResponse({"activeOrders": order_active.data})

@api_view(['POST'])
def get_order_only(request):
	data = request.data
	order = Order.objects.get(id=data['order'])
	order_active = OrderSerializer(order, many=False)
	return JsonResponse({"order": order_active.data})

@api_view(['POST'])
def cancel_order(request):
	data = request.data
	order = Order.objects.get(id=data['order'])
	order.status = 'Отменен'
	if order:
		order.save()
		return Response({'message': 'Order canceled successfully'}, status=status.HTTP_200_OK)
	else:
		return Response({'message': 'Order not canceled successfully'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def apply_order(request):
	data = request.data
	order = Order.objects.get(id=data['order'])
	order.status = 'Завершен'
	if order:
		order.save()
		return Response({'message': 'Order apply successfully'}, status=status.HTTP_200_OK)
	else:
		return Response({'message': 'Order not apply successfully'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def change_status(request):
	data = request.data
	order = Order.objects.get(id=data['order_id'])
	order.status = data['status']
	if order.status == 'В пункте выдачи':
		order.date_delivered = timezone.now()
	if order.status == 'Завершен':
		order.date_of_receiving = timezone.now()
	if order:
		order.save()
		return Response({'message': 'Order edit status successfully'}, status=status.HTTP_200_OK)
	else:
		return Response({'message': 'Order edit status not successfully'}, status=status.HTTP_400_BAD_REQUEST)

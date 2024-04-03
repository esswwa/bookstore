from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
from account.models import User
from basket.models import BasketAdditional
from rest_framework.response import Response
from django.conf import settings
from .models import Order, Address

from .serializers import OrderSerializer, AddressSerializer
from django.core.mail import EmailMultiAlternatives

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

			# subject, from_email, to = "hello", "chitay.letay@mail.ru", "zoom.light@yandex.ru"
			# text_content = "This is an important message."
			# html_content = "<p>This is an <strong>important</strong> message.</p>"
			# msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
			# msg.attach_alternative(html_content, "text/html")
			#
			# # Set the email host user and password
			# msg.connection['username'] = settings.EMAIL_HOST_USER
			# msg.connection['password'] = settings.EMAIL_HOST_PASSWORD
			# msg.send()

			from django.core.mail import send_mail

			response = send_mail(
				"Subject here213213213",
				"Here is the message.dsfdsfdsfsdfdsfdsfdsfds",
				settings.EMAIL_HOST_USER,
				["zoom.light@yandex.ru"],
				fail_silently=False,
			)
			print(response)
			return Response({'message': 'Order added successfully'}, status=status.HTTP_200_OK)
		else:
			return Response({'message': 'Order is not addes'}, status=status.HTTP_400_BAD_REQUEST)
	else:
		return JsonResponse({'message': 'Error basket is empty'}, status=status.HTTP_400_BAD_REQUEST)

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

	user = request.data['user']
	user = User.objects.get(id=user)
	print(user)
	order_active = Order.objects.filter(Q(user=user) & (Q(status='В пути') | Q(status='Оформлен') | Q(status='В пункте выдачи')))

	order_all = Order.objects.filter(user=user)

	order_canceled = Order.objects.filter(Q(user=user) & (Q(status='Отменен') | Q(status='Не выкуплен')))

	order_archive = Order.objects.filter(user=user, status='Завершен')

	for order in order_active:
		if order.status == 'В пункте выдачи':
			if order.date_order_renewal_end_date is None:
				if order.date_delivered < timezone.now() - timedelta(weeks=2):
					order.status = 'Не выкуплен'
					if order:
						order.save()
			else:
				if order.date_order_renewal_end_date <= timezone.now():
					order.status = 'Не выкуплен'
					if order:
						order.save()

	order_all = order_all.order_by('-' +'date_order')
	order_active = order_active.order_by('-' +'date_order')
	order_canceled = order_canceled.order_by('-' +'date_order')
	order_archive = order_archive.order_by('-' +'date_order')

	order_all = OrderSerializer(order_all, many=True)
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
			orders = orders.filter(id=request.data['search_input'])
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
		orders = Order.objects.filter(id=request.data['search_input'])
		count = orders.count()
		start_index = (page - 1) * 12
		end_index = start_index + 12
		if request.data['sort_order'] != 'Без сортировки':
			orders = orders.order_by('-' + request.data['sort_order'])

	if (request.data['sort_order'] == 'Без сортировки'):
		orders = orders.order_by('-' +'date_order')

	orders = orders[start_index:end_index]

	serializer = OrderSerializer(orders, many=True)


	order_active = Order.objects.filter(status='В пункте выдачи')



	for order in order_active:
		if order.status == 'В пункте выдачи':
			if order.date_order_renewal_end_date is None:
				if order.date_delivered < timezone.now() - timedelta(weeks=2):
					order.status = 'Не выкуплен'
					if order:
						order.save()
			else:
				if order.date_order_renewal_end_date <= timezone.now():
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
			order1 = order
			basket_additionals = BasketAdditional.objects.filter(basket=basket_additionals.basket)
			basket_additionals_list = []
			for basket_additional in basket_additionals:
				basket_additionals_list.append({'book': basket_additional.book.id, 'name': Book.objects.get(id=basket_additional.book.id).name, 'count': basket_additional.count,
												'all_price': basket_additional.all_price})
			basket_additionals.delete()
			last_order = Order.objects.filter(user=user).order_by('-id').first()
			last_order.delete()
			order.save()
			order = Order.objects.all().order_by('-id')[0]
			print(order)
			order_id = order
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
		book = Book.objects.get(id=basket_additional['book'].id)
		book.count_on_stock = book.count_on_stock - basket_additional['count']
		print(book.count_on_stock)
		book.save()
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
		import smtplib
		smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
		smtp_server.starttls()
		smtp_server.login("qweq95346@gmail.com", "ynksrgyjulrewmbl")

		from email.mime.multipart import MIMEMultipart
		from email.mime.text import MIMEText

		# Создание объекта сообщения
		msg = MIMEMultipart()

		# Настройка параметров сообщения
		msg["From"] = "Читай-Летай"

		msg["Subject"] = f"Заказ № {order.id}"
		user = User.objects.get(id=order.user_id)
		msg["To"] = user.email
		html = f"""<article style="max-width: 622px;">
			<div>
				<div style="margin:0;padding:0">
				<div style="background-color:#f1f1f1;color:#313131;font-family:'arial' , 'helvetica' , sans-serif;font-size:14px;min-width:300px;width:100%">
					<div style="margin:0 auto 0 auto;max-width:600px">
						<div style="padding-top:50px">
							<table style="width:100%">
								<tbody>
									<tr>
										<td align="center">
											<a href="https://imgbb.com/"><img src="https://i.ibb.co/q1DkZ5K/school-40dp-FILL0-wght400-GRAD0-opsz40.png" alt="school-40dp-FILL0-wght400-GRAD0-opsz40" border="0" /></a>
										</td>
									</tr>
								</tbody>
							</table>
						</div>
						<div style="background-color:#ffffff;padding:30px">
							<div style="line-height:24px;text-align:center">
								<span style="font-size:18px;font-weight:bold">
									Здравствуйте, {user.name}!
								</span>
								<br>
								<span style="font-size:18px">
									По вашей просьбе ваш заказ был отменен.\n
									Благодарим вас за обращение в магазин «Читай-Летай», обращайтесь еще.<br><br>
								</span>
								<span style="font-size:35px;line-height:40px;text-align:center">
									<strong>Номер заказа: <br>№
										<span>{order.id}</span>
									</strong>
								</span>
								<br>
							</div>
							<div style="background-color:#ffffff;padding:30px;color:#b2b2b2;line-height:21px;padding:5px 0 5px 0">
								<strong style="margin-left:30px">ИНФОРМАЦИЯ О ВАШЕМ ЗАКАЗЕ:</strong>
							</div>
							<table style="background-color:#ffffff;padding:30px;border-spacing:0;border-top-color:#e2e3e4;border-top-style:solid;border-top-width:1px;font-size:16px;line-height:24px;width:100%;word-break:break-word;word-wrap:break-word">
								<tbody>
									<tr>
										<th style="height:1px;width:50%"></th>
										<th style="height:1px;width:50%"></th>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Номер заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Счет выставлен:</strong>
										</td>
									</tr>
									<tr>
										<td>
											№<span>{order.id}</span>
										</td>
										<td>
											<span>{user.email}</span>
										</td>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Дата заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Дата отмены заказы:</strong>
										</td>
									</tr>
									<tr>
										<td>{order.date_order.date()}</td>
										<td>{timezone.now().date()}</td>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Новый статус заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Источник</strong>
										</td>
									</tr>
									<tr>
										<td>{order.status}</td>
										<td>Читай-Летай</td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>
				</div>

			</div>
			<div style="background-color:#f1f1f1;">
						<br>
						<br>
						<br>
					</div>
		</article>"""


		# Добавление HTML-содержимого в сообщение
		msg.attach(MIMEText(html, "html"))

		# Отправка письма
		smtp_server.sendmail("qweq95346@gmail.com", user.email, msg.as_string())

		# Закрытие соединения
		smtp_server.quit()
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
		import smtplib
		smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
		smtp_server.starttls()
		smtp_server.login("qweq95346@gmail.com", "ynksrgyjulrewmbl")

		from email.mime.multipart import MIMEMultipart
		from email.mime.text import MIMEText

		# Создание объекта сообщения
		msg = MIMEMultipart()

		# Настройка параметров сообщения
		msg["From"] = "Читай-Летай"

		msg["Subject"] = f"Заказ № {order.id}"
		user = User.objects.get(id=order.user_id)
		msg["To"] = user.email

		html = f"""<article style="max-width: 622px;">
			<div>
				<div style="margin:0;padding:0">
				<div style="background-color:#f1f1f1;color:#313131;font-family:'arial' , 'helvetica' , sans-serif;font-size:14px;min-width:300px;width:100%">
					<div style="margin:0 auto 0 auto;max-width:600px">
						<div style="padding-top:50px">
							<table style="width:100%">
								<tbody>
									<tr>
										<td align="center">
											<a href="https://imgbb.com/"><img src="https://i.ibb.co/q1DkZ5K/school-40dp-FILL0-wght400-GRAD0-opsz40.png" alt="school-40dp-FILL0-wght400-GRAD0-opsz40" border="0" /></a>
										</td>
									</tr>
								</tbody>
							</table>
						</div>
						<div style="background-color:#ffffff;padding:30px">
							<div style="line-height:24px;text-align:center">
								<span style="font-size:18px;font-weight:bold">
									Здравствуйте, {user.name}!
								</span>
								<br>
								<span style="font-size:18px">
									Ваш заказ был выдан!\n
									Благодарим вас за покупку в магазине «Читай-Летай».<br><br>
								</span>
								<span style="font-size:35px;line-height:40px;text-align:center">
									<strong>Номер заказа: <br>№
										<span>{order.id}</span>
									</strong>
								</span>
								<br>
							</div>
							<div style="background-color:#ffffff;padding:30px;color:#b2b2b2;line-height:21px;padding:5px 0 5px 0">
								<strong style="margin-left:30px">ИНФОРМАЦИЯ О ВАШЕМ ЗАКАЗЕ:</strong>
							</div>
							<table style="background-color:#ffffff;padding:30px; border-spacing:0;border-top-color:#e2e3e4;border-top-style:solid;border-top-width:1px;font-size:16px;line-height:24px;width:100%;word-break:break-word;word-wrap:break-word">
								<tbody>
									<tr>
										<th style="height:1px;width:50%"></th>
										<th style="height:1px;width:50%"></th>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Номер заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Счет выставлен:</strong>
										</td>
									</tr>
									<tr>
										<td>
											№<span>{order.id}</span>
										</td>
										<td>
											<span>{user.email}</span>
										</td>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Дата заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Дата получения:</strong>
										</td>
									</tr>
									<tr>
										<td>{order.date_order.date()}</td>
										<td>{timezone.now().date()}</td>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Статус заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Источник</strong>
										</td>
									</tr>
									<tr>
										<td>{order.status}</td>
										<td>Читай-Летай</td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>
				</div>

			</div>
			
		</article>
		<div style="background-color:#f1f1f1;">
						<br>
						<br>
						<br>
					</div>"""

		# Добавление HTML-содержимого в сообщение
		msg.attach(MIMEText(html, "html"))

		# Отправка письма
		smtp_server.sendmail("qweq95346@gmail.com", user.email, msg.as_string())

		# Закрытие соединения
		smtp_server.quit()
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


@api_view(['POST'])
def change_status_send_email(request):
	data = request.data
	order = Order.objects.get(id=data['order_id'])
	order.status = data['status']
	import smtplib
	smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
	smtp_server.starttls()
	smtp_server.login("qweq95346@gmail.com", "ynksrgyjulrewmbl")

	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

	# Создание объекта сообщения
	msg = MIMEMultipart()

	# Настройка параметров сообщения
	msg["From"] = "Читай-Летай"

	msg["Subject"] = f"Заказ № {order.id}"
	user = User.objects.get(id=order.user_id)
	msg["To"] = user.email
	if order.status == 'В пункте выдачи':
		order.date_delivered = timezone.now()
		html = f"""<article style="max-width: 622px;">
			<div>
				<div style="margin:0;padding:0">
				<div style="background-color:#f1f1f1;color:#313131;font-family:'arial' , 'helvetica' , sans-serif;font-size:14px;min-width:300px;width:100%">
					<div style="margin:0 auto 0 auto;max-width:600px">
						<div style="padding-top:50px">
							<table style="width:100%">
								<tbody>
									<tr>
										<td align="center">
											<a href="https://imgbb.com/"><img src="https://i.ibb.co/q1DkZ5K/school-40dp-FILL0-wght400-GRAD0-opsz40.png" alt="school-40dp-FILL0-wght400-GRAD0-opsz40" border="0" /></a>
										</td>
									</tr>
								</tbody>
							</table>
						</div>

						<div style="background-color:#ffffff;padding:30px">
							<div style="line-height:24px;text-align:center">
								<span style="font-size:18px;font-weight:bold">
									Здравствуйте, {user.name}!
								</span>
								<br>
								<span style="font-size:18px">
									Ваш заказ был доставлен в пункт выдачи.
								</span>
					      		<br><br>
								<span style="font-size:35px;line-height:40px;text-align:center">
									<strong>Номер заказа: <br>№
										<span>{order.id}</span>
									</strong>
								</span>
								<br>
							</div>
							<div style="background-color:#ffffff;padding:30px;color:#b2b2b2;line-height:21px;padding:5px 0 5px 0">
								<strong style="margin-left:30px">ИНФОРМАЦИЯ О ВАШЕМ ЗАКАЗЕ:</strong>
							</div>
							<table style="background-color:#ffffff;padding:30px;border-spacing:0;border-top-color:#e2e3e4;border-top-style:solid;border-top-width:1px;font-size:16px;line-height:24px;width:100%;word-break:break-word;word-wrap:break-word">
								<tbody>
									<tr>
										<th style="height:1px;width:50%"></th>
										<th style="height:1px;width:50%"></th>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Номер заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Счет выставлен:</strong>
										</td>
									</tr>
									<tr>
										<td>
											№<span>{order.id}</span>
										</td>
										<td>
											<span>{user.email}</span>
										</td>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Дата заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Дата доставки в пункт выдачи:</strong>
										</td>
									</tr>
									<tr>
										<td>{order.date_order.date()}</td>
										<td>{order.date_delivered.date()}</td>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Новый статус заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Источник</strong>
										</td>
									</tr>
									<tr>
										<td>{order.status}</td>
										<td>Читай-Летай</td>
									</tr>
								</tbody>
							</table>

							<table style="background-color:#ffffff;border-spacing:0;border-top-color:#e2e3e4;border-top-style:solid;border-top-width:1px;line-height:26px;width:100%">
								<tbody>
									<tr>
										<th></th>
									</tr>
									<tr>
										<td style="padding-top:15px;text-align:center">
											В пункте выдачи заказ хранится 14 дней, если в течение 14 дней не получить заказ,
											то он автоматически отменится. Если вы не успеваете его получить, то следует обратиться в службу поддержки.
											Срок хранения заказа смогут продлить до 28 дней.
											<br><br>
										</td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>
					<div style="background-color:#f1f1f1;">
						<br>
						<br>
						<br>
					</div>
				</div>

			</div>
		</article>"""

	# Добавление HTML-содержимого в сообщение

	if order.status == 'Завершен':
		order.date_of_receiving = timezone.now()
		html = f"""<article style="max-width: 622px;">
			<div>
				<div style="margin:0;padding:0">
				<div style="background-color:#f1f1f1;color:#313131;font-family:'arial' , 'helvetica' , sans-serif;font-size:14px;min-width:300px;width:100%">
					<div style="margin:0 auto 0 auto;max-width:600px">
						<div style="padding-top:50px">
							<table style="width:100%">
								<tbody>
									<tr>
										<td align="center">
											<a href="https://imgbb.com/"><img src="https://i.ibb.co/q1DkZ5K/school-40dp-FILL0-wght400-GRAD0-opsz40.png" alt="school-40dp-FILL0-wght400-GRAD0-opsz40" border="0" /></a>
										</td>
									</tr>
								</tbody>
							</table>
						</div>

						<div style="background-color:#ffffff;padding:30px">
							<div style="line-height:24px;text-align:center">
								<span style="font-size:18px;font-weight:bold">
									Здравствуйте, {user.name}!
								</span>
								<br>
								<span style="font-size:18px">
									Ваш заказ был выдан!\n
									Благодарим вас за покупку в магазине «Читай-Летай».<br><br>
								</span>
								<span style="font-size:35px;line-height:40px;text-align:center">
									<strong>Номер заказа: <br>№
										<span>{order.id}</span>
									</strong>
								</span>
								<br>
							</div>
							<div style="background-color:#ffffff;padding:30px;color:#b2b2b2;line-height:21px;padding:5px 0 5px 0">
								<strong style="margin-left:30px">ИНФОРМАЦИЯ О ВАШЕМ ЗАКАЗЕ:</strong>
							</div>
							<table style="background-color:#ffffff;padding:30px;border-spacing:0;border-top-color:#e2e3e4;border-top-style:solid;border-top-width:1px;font-size:16px;line-height:24px;width:100%;word-break:break-word;word-wrap:break-word">
								<tbody>
									<tr>
										<th style="height:1px;width:50%"></th>
										<th style="height:1px;width:50%"></th>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Номер заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Счет выставлен:</strong>
										</td>
									</tr>
									<tr>
										<td>
											№<span>{order.id}</span>
										</td>
										<td>
											<span>{user.email}</span>
										</td>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Дата заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Дата получения:</strong>
										</td>
									</tr>
									<tr>
										<td>{order.date_order.date()}</td>
										<td>{timezone.now().date()}</td>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Статус заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Источник</strong>
										</td>
									</tr>
									<tr>
										<td>{order.status}</td>
										<td>Читай-Летай</td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>
				</div>

			</div>
			<div style="background-color:#f1f1f1;">
						<br>
						<br>
						<br>
					</div>
		</article>"""

	if order.status == 'В пути':
		html = f"""<article style="max-width: 622px;">
			<div>
				<div style="margin:0;padding:0">
				<div style="background-color:#f1f1f1;color:#313131;font-family:'arial' , 'helvetica' , sans-serif;font-size:14px;min-width:300px;width:100%">
					<div style="margin:0 auto 0 auto;max-width:600px">
						<div style="padding-top:50px">
							<table style="width:100%">
								<tbody>
									<tr>
										<td align="center">
											<a href="https://imgbb.com/"><img src="https://i.ibb.co/q1DkZ5K/school-40dp-FILL0-wght400-GRAD0-opsz40.png" alt="school-40dp-FILL0-wght400-GRAD0-opsz40" border="0" /></a>
										</td>
									</tr>
								</tbody>
							</table>
						</div>

						<div style="background-color:#ffffff;padding:30px">
							<div style="line-height:24px;text-align:center">
								<span style="font-size:18px;font-weight:bold">
									Здравствуйте, {user.name}!
								</span>
								<br>
								<span style="font-size:18px">
									Ваш заказ был передан в доставку.
								</span>
					      		<br><br>
								<span style="font-size:35px;line-height:40px;text-align:center">
									<strong>Номер заказа: <br>№
										<span>{order.id}</span>
									</strong>
								</span>
								<br>
							</div>
							<div style="background-color:#ffffff;padding:30px;color:#b2b2b2;line-height:21px;padding:5px 0 5px 0">
								<strong style="margin-left:30px">ИНФОРМАЦИЯ О ВАШЕМ ЗАКАЗЕ:</strong>
							</div>
							<table style="background-color:#ffffff;padding:30px;border-spacing:0;border-top-color:#e2e3e4;border-top-style:solid;border-top-width:1px;font-size:16px;line-height:24px;width:100%;word-break:break-word;word-wrap:break-word">
								<tbody>
									<tr>
										<th style="height:1px;width:50%"></th>
										<th style="height:1px;width:50%"></th>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Номер заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Счет выставлен:</strong>
										</td>
									</tr>
									<tr>
										<td>
											№<span>{order.id}</span>
										</td>
										<td>
											<span>{user.email}</span>
										</td>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Дата заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Планируемая дата доставки:</strong>
										</td>
									</tr>
									<tr>
										<td>{order.date_order.date()}</td>
										<td>{order.date_order.date() + timedelta(days=10)}</td>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Новый статус заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Источник</strong>
										</td>
									</tr>
									<tr>
										<td>{order.status}</td>
										<td>Читай-Летай</td>
									</tr>
								</tbody>
							</table>

							<table style="background-color:#ffffff;border-spacing:0;border-top-color:#e2e3e4;border-top-style:solid;border-top-width:1px;line-height:26px;width:100%">
								<tbody>
								<tr>
									<th></th>
								</tr>
								<tr>
									<td style="padding-top:15px;text-align:center">
										В пункте выдачи заказ хранится 14 дней, если в течение 14 дней не получить заказ,
										то он автоматически отменится. Если вы не успеваете его получить, то следует обратиться в службу поддержки.
										Срок хранения заказа смогут продлить до 28 дней.
										<br><br>
									</td>
								</tr>
							</tbody>
							</table>
						</div>
					</div>
					<div style="background-color:#f1f1f1;">
						<br>
						<br>
						<br>
					</div>
				</div>

			</div>
		</article>"""
	if order.status == "Не выкуплен":
		html = f"""<article style="max-width: 622px;">
			<div>
				<div style="margin:0;padding:0">
				<div style="background-color:#f1f1f1;color:#313131;font-family:'arial' , 'helvetica' , sans-serif;font-size:14px;min-width:300px;width:100%">
					<div style="margin:0 auto 0 auto;max-width:600px">
						<div style="padding-top:50px">
							<table style="width:100%">
								<tbody>
									<tr>
										<td align="center">
											<a href="https://imgbb.com/"><img src="https://i.ibb.co/q1DkZ5K/school-40dp-FILL0-wght400-GRAD0-opsz40.png" alt="school-40dp-FILL0-wght400-GRAD0-opsz40" border="0" /></a>
										</td>
									</tr>
								</tbody>
							</table>
						</div>

						<div style="background-color:#ffffff;padding:30px">
							<div style="line-height:24px;text-align:center">
								<span style="font-size:18px;font-weight:bold">
									Здравствуйте, {user.name}!
								</span>
								<br>
								<span style="font-size:18px">
									К сожалению, так как вы не забрали свой заказ\n
									в течение 14 дней с момента покупки, книги отправлены на склад.\n
								Благодарим вас за обращение в магазин «Читай-Летай», обращайтесь еще.<br><br>
								</span>
								<span style="font-size:35px;line-height:40px;text-align:center">
									<strong>Номер заказа: <br>№
										<span>{order.id}</span>
									</strong>
								</span>
								<br>
							</div>
							<div style="background-color:#ffffff;padding:30px;color:#b2b2b2;line-height:21px;padding:5px 0 5px 0">
								<strong style="margin-left:30px">ИНФОРМАЦИЯ О ВАШЕМ ЗАКАЗЕ:</strong>
							</div>
							<table style="background-color:#ffffff;padding:30px;border-spacing:0;border-top-color:#e2e3e4;border-top-style:solid;border-top-width:1px;font-size:16px;line-height:24px;margin-bottom:20px;width:100%;word-break:break-word;word-wrap:break-word">
								<tbody>
									<tr>
										<th style="height:1px;width:50%"></th>
										<th style="height:1px;width:50%"></th>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Номер заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Счет выставлен:</strong>
										</td>
									</tr>
									<tr>
										<td>
											№<span>{order.id}</span>
										</td>
										<td>
											<span>{user.email}</span>
										</td>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Дата заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Дата отмены заказы:</strong>
										</td>
									</tr>
									<tr>
										<td>{order.date_order.date()}</td>
										<td>{timezone.now().date()}</td>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Новый статус заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Источник</strong>
										</td>
									</tr>
									<tr>
										<td>{order.status}</td>
										<td>Читай-Летай</td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>
				</div>

			</div>
			<div style="background-color:#f1f1f1;">
						<br>
						<br>
						<br>
					</div>
		</article>"""
	if order.status == "Отменен":
		html = f"""<article style="max-width: 622px;">
				<div>
					<div style="margin:0;padding:0">
						<div style="background-color:#f1f1f1;color:#313131;font-family:'arial' , 'helvetica' , sans-serif;font-size:14px;min-width:300px;width:100%">
							<div style="margin:0 auto 0 auto;max-width:600px">
								<div style="padding-top:50px">
									<table style="width:100%">
										<tbody>
											<tr>
												<td align="center">
													<a href="https://imgbb.com/"><img src="https://i.ibb.co/q1DkZ5K/school-40dp-FILL0-wght400-GRAD0-opsz40.png" alt="school-40dp-FILL0-wght400-GRAD0-opsz40" border="0" /></a>
												</td>
											</tr>
										</tbody>
									</table>
								</div>

								<div style="background-color:#ffffff;padding:30px">
									<div style="line-height:24px;text-align:center">
										<span style="font-size:18px;font-weight:bold">
											Здравствуйте, {user.name}!
										</span>
										<br>
										<span style="font-size:18px">
											По вашей просьбе ваш заказ был отменен.\n
											Благодарим вас за обращение в магазин «Читай-Летай», обращайтесь еще.<br><br>
										</span>
										<span style="font-size:35px;line-height:40px;text-align:center">
											<strong>Номер заказа: <br>№
												<span>{order.id}</span>
											</strong>
										</span>
										<br>
									</div>
									<div style="background-color:#ffffff;padding:30px;color:#b2b2b2;line-height:21px;padding:5px 0 5px 0">
										<strong style="margin-left:30px">ИНФОРМАЦИЯ О ВАШЕМ ЗАКАЗЕ:</strong>
									</div>
									<table style="background-color:#ffffff;padding:30px;border-spacing:0;border-top-color:#e2e3e4;border-top-style:solid;border-top-width:1px;font-size:16px;line-height:24px;width:100%;word-break:break-word;word-wrap:break-word">
										<tbody>
											<tr>
												<th style="height:1px;width:50%"></th>
												<th style="height:1px;width:50%"></th>
											</tr>
											<tr>
												<td style="padding-top:15px">
													<strong>Номер заказа:</strong>
												</td>
												<td style="padding-top:15px">
													<strong>Счет выставлен:</strong>
												</td>
											</tr>
											<tr>
												<td>
													№<span>{order.id}</span>
												</td>
												<td>
													<span>{user.email}</span>
												</td>
											</tr>
											<tr>
												<td style="padding-top:15px">
													<strong>Дата заказа:</strong>
												</td>
												<td style="padding-top:15px">
													<strong>Дата отмены заказы:</strong>
												</td>
											</tr>
											<tr>
												<td>{order.date_order.date()}</td>
												<td>{timezone.now().date()}</td>
											</tr>
											<tr>
												<td style="padding-top:15px">
													<strong>Новый статус заказа:</strong>
												</td>
												<td style="padding-top:15px">
													<strong>Источник</strong>
												</td>
											</tr>
											<tr>
												<td>{order.status}</td>
												<td>Читай-Летай</td>
											</tr>
										</tbody>
									</table>
								</div>
							</div>
						</div>
					</div>
					<div style="background-color:#f1f1f1;">
						<br>
						<br>
						<br>
					</div>
				</article>"""

	msg.attach(MIMEText(html, "html"))

	# Отправка письма
	smtp_server.sendmail("qweq95346@gmail.com", user.email, msg.as_string())

	# Закрытие соединения
	smtp_server.quit()
	return Response({'message': 'Email send'}, status=status.HTTP_200_OK)
@api_view(['POST'])
def order_renewal_date(request):
	data = request.data
	order = Order.objects.get(id=data['order_id'])
	date = data['date']
	order.date_order_renewal_end_date = order.date_delivered + timezone.timedelta(days=(int(date) + 14))

	import smtplib
	smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
	smtp_server.starttls()
	smtp_server.login("qweq95346@gmail.com", "ynksrgyjulrewmbl")

	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

	# Создание объекта сообщения
	msg = MIMEMultipart()

	# Настройка параметров сообщения
	msg["From"] = "Читай-Летай"

	msg["Subject"] = f"Заказ № {order.id}"
	user = User.objects.get(id=order.user_id)
	msg["To"] = user.email
	if order:
		order.save()

		html = f"""<article style="max-width: 622px;">
			<div>
				<div style="margin:0;padding:0">
				<div style="background-color:#f1f1f1;color:#313131;font-family:'arial' , 'helvetica' , sans-serif;font-size:14px;min-width:300px;width:100%">
					<div style="margin:0 auto 0 auto;max-width:600px">
						<div style="padding-top:50px">
							<table style="width:100%">
								<tbody>
									<tr>
										<td align="center">
											<a href="https://imgbb.com/"><img src="https://i.ibb.co/q1DkZ5K/school-40dp-FILL0-wght400-GRAD0-opsz40.png" alt="school-40dp-FILL0-wght400-GRAD0-opsz40" border="0" /></a>
										</td>
									</tr>
								</tbody>
							</table>
						</div>

						<div style="background-color:#ffffff;padding:30px">
							<div style="line-height:24px;text-align:center">
								<span style="font-size:18px;font-weight:bold">
									Здравствуйте, {user.name}!
								</span>
								<br>
								<span style="font-size:18px">
									По вашей просьбе срок хранения заказа был продлен.
								</span>
					      		<br><br>
								<span style="font-size:35px;line-height:40px;text-align:center">
									<strong>Номер заказа: <br>№
										<span>{order.id}</span>
									</strong>
								</span>
								<br>
							</div>
							<div style="background-color:#ffffff;padding:30px;color:#b2b2b2;line-height:21px;padding:5px 0 5px 0">
								<strong style="margin-left:30px">ИНФОРМАЦИЯ О ВАШЕМ ЗАКАЗЕ:</strong>
							</div>
							<table style="background-color:#ffffff;padding:30px;border-spacing:0;border-top-color:#e2e3e4;border-top-style:solid;border-top-width:1px;font-size:16px;line-height:24px;width:100%;word-break:break-word;word-wrap:break-word">
								<tbody>
									<tr>
										<th style="height:1px;width:50%"></th>
										<th style="height:1px;width:50%"></th>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Номер заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Счет выставлен:</strong>
										</td>
									</tr>
									<tr>
										<td>
											№<span>{order.id}</span>
										</td>
										<td>
											<span>{user.email}</span>
										</td>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Дата заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Новый срок хранения заказа по:</strong>
										</td>
									</tr>
									<tr>
										<td>{order.date_order.date()}</td>
										<td>{order.date_order_renewal_end_date.date()}</td>
									</tr>
									<tr>
										<td style="padding-top:15px">
											<strong>Новый статус заказа:</strong>
										</td>
										<td style="padding-top:15px">
											<strong>Источник</strong>
										</td>
									</tr>
									<tr>
										<td>{order.status}</td>
										<td>Читай-Летай</td>
									</tr>
								</tbody>
							</table>

							<table style="background-color:#ffffff;border-spacing:0;border-top-color:#e2e3e4;border-top-style:solid;border-top-width:1px;line-height:26px;width:100%">
								<tbody>
									<tr>
										<th></th>
									</tr>
									<tr>
										<td style="padding-top:15px;text-align:center">
											В пункте выдачи заказ хранится 14 дней, если в течение 14 дней не получить заказ,
											то он автоматически отменится. Если вы не успеваете его получить, то следует обратиться в службу поддержки.
											Срок хранения заказа смогут продлить до 28 дней.
											<br><br>
										</td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>
					<div style="background-color:#f1f1f1;">
						<br>
						<br>
						<br>
					</div>
				</div>

			</div>
		</article>"""

		msg.attach(MIMEText(html, "html"))

		# Отправка письма
		smtp_server.sendmail("qweq95346@gmail.com", user.email, msg.as_string())

		# Закрытие соединения
		smtp_server.quit()
		return Response({'message': 'Order edit status successfully'}, status=status.HTTP_200_OK)
	else:
		return Response({'message': 'Order edit status not successfully'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def send_message(request):
	data = request.data

	basket_additionals_list = data['basket_additionals_list']

	order_id = data['order_id']
	order1 = data['order1']
	order1 = Order.objects.get(id=order1)
	user = User.objects.get(id=data['user'])
	import smtplib

	smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
	smtp_server.starttls()
	smtp_server.login("qweq95346@gmail.com", "ynksrgyjulrewmbl")

	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

	# Создание объекта сообщения
	msg = MIMEMultipart()

	# Настройка параметров сообщения
	msg["From"] = "Читай-Летай"
	msg["To"] = user.email
	msg["Subject"] = f"Заказ № {order_id}"

	# Добавление текста в сообщение
	# Создание HTML-содержимого письма

	html = f"""<article style="max-width: 622px;">
		<div>
			<div style="margin:0;padding:0">
			<div style="background-color:#f1f1f1;color:#313131;font-family:'arial' , 'helvetica' , sans-serif;font-size:14px;min-width:300px;width:100%">
				<div style="margin:0 auto 0 auto;max-width:600px">
					<div style="padding-top:50px">
						<table style="width:100%">
							<tbody>
								<tr>
									<td align="center">
										<a href="https://imgbb.com/"><img src="https://i.ibb.co/q1DkZ5K/school-40dp-FILL0-wght400-GRAD0-opsz40.png" alt="school-40dp-FILL0-wght400-GRAD0-opsz40" border="0" /></a>
									</td>
								</tr>
							</tbody>
						</table>
					</div>
		
					<div style="background-color:#ffffff;padding:30px">
						<div style="line-height:24px;text-align:center">
							<span style="font-size:18px;font-weight:bold">
								Здравствуйте, {user.name}!
							</span>
							<br>
							Благодарим вас за покупку в магазине «Читай-Летай».<br><br>
							<span style="font-size:35px;line-height:40px;text-align:center">
								<strong>Номер заказа: <br>№
									<span>{order_id}</span>
								</strong>
							</span>
							<br>
						</div>
						<div style="color:#b2b2b2;line-height:21px;padding:5px 0 5px 0">
							<strong>ИНФОРМАЦИЯ О ВАШЕМ ЗАКАЗЕ:</strong>
						</div>
						<table style="border-spacing:0;border-top-color:#e2e3e4;border-top-style:solid;border-top-width:1px;font-size:16px;line-height:24px;margin-bottom:20px;width:100%;word-break:break-word;word-wrap:break-word">
							<tbody>
								<tr>
									<th style="height:1px;width:50%"></th>
									<th style="height:1px;width:50%"></th>
								</tr>
								<tr>
									<td style="padding-top:15px">
										<strong>Номер заказа:</strong>
									</td>
									<td style="padding-top:15px">
										<strong>Счет выставлен:</strong>
									</td>
								</tr>
								<tr>
									<td>
										№<span>{order_id}</span>
									</td>
									<td>
										<span>{user.email}</span>
									</td>
								</tr>
								<tr>
									<td style="padding-top:15px">
										<strong>Дата заказа:</strong>
									</td>
									<td style="padding-top:15px">
										<strong>Источник:</strong>
									</td>
								</tr>
								<tr>
									<td>{order1.date_order.date()}</td>
									<td>Читай-Летай</td>
								</tr>
							</tbody>
						</table>
		
		
						<div style="color:#b2b2b2;line-height:21px;padding:5px 0 5px 0">
							<strong>СОДЕРЖИМОЕ ВАШЕГО ЗАКАЗА:</strong>
						</div>
						<table style="border-spacing:0;border-top-color:#e2e3e4;border-top-style:solid;border-top-width:1px;margin-bottom:20px;width:100%">
							<tbody>
								<tr style="background-color:#f1f1f1">
									<th style="min-width:100px;padding:10px 0 10px 10px;text-align:left;vertical-align:top">Название книги:</th>
									<th style="min-width:80px;padding:10px 0 10px 10px;text-align:left;vertical-align:top">Количество:</th>
									<th style="padding:10px 10px 10px 0;text-align:right;vertical-align:top">Сумма:</th>
								</tr>
								<tbody>
									{' '.join([
										f"""
											<tr>
											  <td style="max-width:200px;padding-left:10px;padding-top:15px;word-break:break-all">{book['name']}</td>
											  <td style="padding-left:10px; text-align:center; padding-top:15px;word-break:break-all">{book['count']}</td>
											  <td style="padding-left:10px; text-align:center;padding-top:15px;word-break:break-all">{book['all_price']:.2f} ₽</td>
											</tr>
										"""
										for book in basket_additionals_list
									])}
				      			</tbody>
							</tbody>
						</table>
						<table style="border-spacing:0;border-top-color:#e2e3e4;border-top-style:solid;border-top-width:1px;line-height:26px;margin-bottom:20px;text-align:right;width:100%">
							<tbody>
							<tr>
								<th></th>
								<th style="width:1%"></th>
							</tr>
							<tr>
								<td style="padding-top:15px">
									<span style="color:#b2b2b2;font-weight:bold;text-transform:uppercase">ИТОГО:</span>
								</td>
								<td style="padding:15px 10px 0 10px">
									<span style="font-weight:bold">{order1.all_price}&nbsp;RUB</span>
								</td>
							</tr>
							<tr><td colspan="2" style="padding-top:15px;text-align:center"></td></tr>
							</tbody>
						</table>
		
		
						<table style="border-spacing:0;border-top-color:#e2e3e4;border-top-style:solid;border-top-width:1px;line-height:26px;margin-bottom:20px;width:100%">
							<tbody>
								<tr>
									<th></th>
								</tr>
								<tr>
									<td style="padding-top:15px;text-align:center">Советуем сохранить копию данного чека для отчетности.</td>
								</tr>
								<tr>
									<td style="padding-top:15px;text-align:center">
										<a href="http://localhost:5173/profile/{user.id}">Посмотреть все свои заказы</a>
									</td>
								</tr>
							</tbody>
						</table>
		
						<table style="background-color:#ffffff;border-spacing:0;border-top-color:#e2e3e4;border-top-style:solid;border-top-width:1px;line-height:26px;margin-bottom:20px;width:100%">
							<tbody>
								<tr>
									<th></th>
								</tr>
								<tr>
									<td style="padding-top:15px;text-align:center">
										<div class="delivery-date">Ориентировочная дата доставки: {(order1.date_order + timezone.timedelta(days=10)).date()}</div>
										<br>
										В пункте выдачи заказ хранится 14 дней, если в течение 14 дней не получить заказ,
										то он автоматически отменится. Если вы не успеваете его получить, то следует обратиться в службу поддержки.
										Срок хранения заказа смогут продлить до 28 дней.
									</td>
								</tr>
							</tbody>
						</table>
					</div>
				</div>
			</div>
	
		</div>
		<div style="background-color:#f1f1f1;">
			<br>
			<br>
			<br>
		</div>
	</article>"""

	# Добавление HTML-содержимого в сообщение
	msg.attach(MIMEText(html, "html"))

	# Отправка письма
	smtp_server.sendmail("qweq95346@gmail.com", user.email, msg.as_string())

	# Закрытие соединения
	smtp_server.quit()
	return Response({'message': 'Message send'}, status=status.HTTP_200_OK)
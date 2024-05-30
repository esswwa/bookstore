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

	import smtplib

	smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
	smtp_server.starttls()
	smtp_server.login("qweq95346@gmail.com", "ynksrgyjulrewmbl")

	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

	# Создание объекта сообщения
	msg = MIMEMultipart()

	# Настройка параметров сообщения
	msg["From"] = "qweq95346@gmail.com"

	for order in order_active:
		if order.status == 'В пункте выдачи':
			msg["Subject"] = f"Заказ № {order.id}"
			user = User.objects.get(id=order.user_id).email
			msg["To"] = user
			if order.date_order_renewal_end_date is None:
				if order.date_delivered < timezone.now() - timedelta(weeks=2):
					order.status = 'Не выкуплен'
					if order:
						order.save()
						html = f"""
									<!DOCTYPE html>
									<html>
									<head>
									  <meta charset="UTF-8">
									  <title>Заказ № {order.id}</title>
						  				<link rel="stylesheet" href="style.css">
									</head>
									<body>
									  <div class="container">
									    <h1>Информация о вашем заказе № {order.id}</h1>
									    <div class="total">К сожалению, так как вы не забрали свой заказ\n
									      в течение 14 дней с момента покупки, книги были отправлены на склад.</div>
									      <br/>
									    <div>Надеемся, что вы повторите свой заказ:)</div>
									  </div>
									</body>
									</html>
									"""

						# Добавление HTML-содержимого в сообщение
						msg.attach(MIMEText(html, "html"))

						# Отправка письма
						smtp_server.sendmail("qweq95346@gmail.com", user, msg.as_string())

						# Закрытие соединения
						smtp_server.quit()
			else:
				if order.date_order_renewal_end_date <= timezone.now():
					order.status = 'Не выкуплен'
					if order:
						html = f"""
															<!DOCTYPE html>
															<html>
															<head>
															  <meta charset="UTF-8">
															  <title>Заказ № {order.id}</title>
												  				<link rel="stylesheet" href="style.css">
															</head>
															<body>
															  <div class="container">
															    <h1>Информация о вашем заказе № {order.id}</h1>
															    <div class="total">К сожалению, так как вы не забрали свой заказ\n
															      в течение 14 дней с момента покупки, книги были отправлены на склад.</div>
															      <br/>
															    <div>Надеемся, что вы повторите свой заказ:)</div>
															  </div>
															</body>
															</html>
															"""

						# Добавление HTML-содержимого в сообщение
						msg.attach(MIMEText(html, "html"))

						# Отправка письма
						smtp_server.sendmail("qweq95346@gmail.com", user, msg.as_string())

						# Закрытие соединения
						smtp_server.quit()
						order.save()

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
			orders = orders.filter(id__in=request.data['search_input'])
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

	orders = orders[start_index:end_index]

	serializer = OrderSerializer(orders, many=True)


	order_active = Order.objects.filter(status='В пункте выдачи')

	import smtplib

	smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
	smtp_server.starttls()
	smtp_server.login("qweq95346@gmail.com", "ynksrgyjulrewmbl")

	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

	# Создание объекта сообщения
	msg = MIMEMultipart()

	# Настройка параметров сообщения
	msg["From"] = "qweq95346@gmail.com"

	for order in order_active:
		if order.status == 'В пункте выдачи':
			msg["Subject"] = f"Заказ № {order.id}"
			user = User.objects.get(id=order.user_id).email
			msg["To"] = user
			if order.date_order_renewal_end_date is None:
				if order.date_delivered < timezone.now() - timedelta(weeks=2):
					order.status = 'Не выкуплен'
					if order:
						order.save()
						html = f"""
						<!DOCTYPE html>
						<html>
						<head>
						  <meta charset="UTF-8">
						  <title>Заказ № {order.id}</title>
							<link rel="stylesheet" href="style.css">
						</head>
						<body>
						  <div class="container">
						    <h1>Информация о вашем заказе № {order.id}</h1>
						    <div class="total">К сожалению, так как вы не забрали свой заказ\n
						      в течение 14 дней с момента покупки, книги были отправлены на склад.</div>
						      <br/>
						    <div>Надеемся, что вы повторите свой заказ:)</div>
						  </div>
						</body>
						</html>
						"""

						# Добавление HTML-содержимого в сообщение
						msg.attach(MIMEText(html, "html"))

						# Отправка письма
						smtp_server.sendmail("qweq95346@gmail.com", user, msg.as_string())

						# Закрытие соединения
						smtp_server.quit()
			else:
				if order.date_order_renewal_end_date <= timezone.now():
					order.status = 'Не выкуплен'
					if order:
						html = f"""
						<!DOCTYPE html>
						<html>
						<head>
						  <meta charset="UTF-8">
						  <title>Заказ № {order.id}</title>
							<link rel="stylesheet" href="style.css">
						</head>
						<body>
						  <div class="container">
						    <h1>Информация о вашем заказе № {order.id}</h1>
						    <div class="total">К сожалению, так как вы не забрали свой заказ\n
						      в течение 14 дней с момента покупки, книги были отправлены на склад.</div>
						      <br/>
						    <div>Надеемся, что вы повторите свой заказ:)</div>
						  </div>
						</body>
						</html>
						"""

						# Добавление HTML-содержимого в сообщение
						msg.attach(MIMEText(html, "html"))

						# Отправка письма
						smtp_server.sendmail("qweq95346@gmail.com", user, msg.as_string())

						# Закрытие соединения
						smtp_server.quit()
						order.save()

	return JsonResponse({"orders": serializer.data, 'count': count}, safe=False)



@api_view(['GET'])
def get_address(request):

	address = Address.objects.all()
	serializer = AddressSerializer(address, many=True)

	return JsonResponse({"address": serializer.data})


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
	msg["From"] = "qweq95346@gmail.com"
	msg["To"] = user.email
	msg["Subject"] = f"Заказ № {order_id}"

	# Добавление текста в сообщение
	# Создание HTML-содержимого письма
	html = f"""
				<!DOCTYPE html>
				<html>
				<head>
				  <meta charset="UTF-8">
				  <title>Чек на покупку книг</title>
	  				<link rel="stylesheet" href="style.css">
				</head>
				<body>
				  <div class="container">
				    <h1>Чек на покупку книг</h1>
				    <table>
				      <thead>
				        <tr>
				          <th>Название книги</th>
				          <th>Количество</th>
				          <th>Сумма</th>
				          <th>Изображение</th>
				        </tr>
				      </thead>
				      <tbody>
				       {' '.join([
		f"""
							<tr>
							  <td>{book['name']}</td>
							  <td>{book['count']}</td>
							  <td>{book['all_price']:.2f} ₽</td>
							  <td>
							  <img class="p-2" style="height: 70px; width: 50px;" :src="require(`./frontend/src/assets/img/${book['book']}.jpg`).url" alt="Изображение">
							  </td>
							</tr>
							"""
		for book in basket_additionals_list
	])}
				      </tbody>
				    </table>
				    <div class="total">Итого: {order1.all_price} ₽</div>
				    <div class="delivery-date">Ориентировочная дата доставки: {(order1.date_order + timezone.timedelta(days=10)).date()}</div>
				    <div class="thank-you">Спасибо за покупку! Приятного чтения!</div>
				  </div>
				</body>
				</html>
				"""

	# Добавление HTML-содержимого в сообщение
	msg.attach(MIMEText(html, "html"))

	# Отправка письма
	smtp_server.sendmail("qweq95346@gmail.com", user.email, msg.as_string())

	# Закрытие соединения
	smtp_server.quit()
	return Response({'message': 'Message send'}, status=status.HTTP_200_OK)

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
		msg["From"] = "qweq95346@gmail.com"

		msg["Subject"] = f"Заказ № {order.id}"
		user = User.objects.get(id=order.user_id).email
		msg["To"] = user
		html = f"""
			<!DOCTYPE html>
			<html>
			<head>
			  <meta charset="UTF-8">
			  <title>Заказ № {order.id}</title>
				<link rel="stylesheet" href="style.css">
			</head>
			<body>
			  <div class="container">
			    <h1>Информация о вашем заказе № {order.id}</h1>
			    <div class="total">Ваш заказ был отменен.</div>
			      <br/>
			    <div>Надеемся, что вы повторите свой заказ:)</div>
			  </div>
			</body>
			</html>
			"""

		# Добавление HTML-содержимого в сообщение
		msg.attach(MIMEText(html, "html"))

		# Отправка письма
		smtp_server.sendmail("qweq95346@gmail.com", user, msg.as_string())

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
		msg["From"] = "qweq95346@gmail.com"

		msg["Subject"] = f"Заказ № {order.id}"
		user = User.objects.get(id=order.user_id).email
		msg["To"] = user
		html = f"""
					<!DOCTYPE html>
					<html>
					<head>
					  <meta charset="UTF-8">
					  <title>Заказ № {order.id}</title>
						<link rel="stylesheet" href="style.css">
					</head>
					<body>
					  <div class="container">
					    <h1>Информация о вашем заказе № {order.id}</h1>
					    <div class="total">Ваш заказ был получен. Дата получения: {order.date_of_receiving.date()}</div>
					      <br/>
					    <div>Спасибо, что вы выбрали наш магазин, до скорых встреч!</div>
					  </div>
					</body>
					</html>
					"""

		# Добавление HTML-содержимого в сообщение
		msg.attach(MIMEText(html, "html"))

		# Отправка письма
		smtp_server.sendmail("qweq95346@gmail.com", user, msg.as_string())

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
	import smtplib
	smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
	smtp_server.starttls()
	smtp_server.login("qweq95346@gmail.com", "ynksrgyjulrewmbl")

	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText

	# Создание объекта сообщения
	msg = MIMEMultipart()

	# Настройка параметров сообщения
	msg["From"] = "qweq95346@gmail.com"

	msg["Subject"] = f"Заказ № {order.id}"
	user = User.objects.get(id=order.user_id).email
	msg["To"] = user
	if order.status == 'В пункте выдачи':
		order.date_delivered = timezone.now()

		html = f"""
					<!DOCTYPE html>
					<html>
					<head>
					  <meta charset="UTF-8">
					  <title>Заказ № {order.id}</title>
						<link rel="stylesheet" href="style.css">
					</head>
					<body>
					  <div class="container">
					    <h1>Информация о вашем заказе № {order.id}</h1>
					    <div class="total">Ваш заказ был доставлен в пункт выдачи. Дата доставки: {order.date_delivered.date()}</div>
					    <div>
						  Если вы не заберете заказ в течении<br>
						  2-х недель, то он будет автоматически отменен!
					      <br/>
						  Если вы хотите продлить хранения заказа,<br>
						  то необходимо связаться с оператором нашего магазина.
					    </div>
					      <br/>
					    <div>Спасибо, что вы выбрали наш магазин, ждем вас с нетерпением!</div>
					  </div>
					</body>
					</html>
					"""

		# Добавление HTML-содержимого в сообщение

	if order.status == 'Завершен':
		order.date_of_receiving = timezone.now()
		html = f"""
							<!DOCTYPE html>
							<html>
							<head>
							  <meta charset="UTF-8">
							  <title>Заказ № {order.id}</title>
								<link rel="stylesheet" href="style.css">
							</head>
							<body>
							  <div class="container">
							    <h1>Информация о вашем заказе № {order.id}</h1>
							    <div class="total">Ваш заказ был получен. Дата получения: {order.date_of_receiving.date()}</div>
							      <br/>
							    <div>Спасибо, что вы выбрали наш магазин, до скорых встреч!</div>
							  </div>
							</body>
							</html>
							"""
	if order.status == 'В пути':
		html = f"""
							<!DOCTYPE html>
							<html>
							<head>
							  <meta charset="UTF-8">
							  <title>Заказ № {order.id}</title>
								<link rel="stylesheet" href="style.css">
							</head>
							<body>
							  <div class="container">
							    <h1>Информация о вашем заказе № {order.id}</h1>
							    <div class="total">Ваш заказ был передан в доставку.</div>
							    <div>
								 	Планируемая дата доставки: {order.date_order.date() + timedelta(days=10)}
							    </div>
							      <br/>
							    <div>Спасибо, что вы выбрали наш магазин!</div>
							  </div>
							</body>
							</html>
							"""
	if order.status == "Не выкуплен":
		html = f"""
								<!DOCTYPE html>
								<html>
								<head>
								  <meta charset="UTF-8">
								  <title>Заказ № {order.id}</title>
									<link rel="stylesheet" href="style.css">
								</head>
								<body>
								  <div class="container">
								    <h1>Информация о вашем заказе № {order.id}</h1>
								    <div class="total">К сожалению, так как вы не забрали свой заказ\n
								      в течение 14 дней с момента покупки, книги были отправлены на склад.</div>
								      <br/>
								    <div>Надеемся, что вы повторите свой заказ:)</div>
								  </div>
								</body>
								</html>
								"""
	if order.status == "Отменен":
		html = f"""
					<!DOCTYPE html>
					<html>
					<head>
					  <meta charset="UTF-8">
					  <title>Заказ № {order.id}</title>
						<link rel="stylesheet" href="style.css">
					</head>
					<body>
					  <div class="container">
					    <h1>Информация о вашем заказе № {order.id}</h1>
					    <div class="total">Ваш заказ был отменен.</div>
					      <br/>
					    <div>Надеемся, что вы повторите свой заказ:)</div>
					  </div>
					</body>
					</html>
					"""
	if order:
		order.save()
		msg.attach(MIMEText(html, "html"))

		# Отправка письма
		smtp_server.sendmail("qweq95346@gmail.com", user, msg.as_string())

		# Закрытие соединения
		smtp_server.quit()
		return Response({'message': 'Order edit status successfully'}, status=status.HTTP_200_OK)
	else:
		return Response({'message': 'Order edit status not successfully'}, status=status.HTTP_400_BAD_REQUEST)

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
	msg["From"] = "qweq95346@gmail.com"

	msg["Subject"] = f"Заказ № {order.id}"
	user = User.objects.get(id=order.user_id).email
	msg["To"] = user
	if order:
		order.save()
		html = f"""
							<!DOCTYPE html>
							<html>
							<head>
							  <meta charset="UTF-8">
							  <title>Заказ № {order.id}</title>
								<link rel="stylesheet" href="style.css">
							</head>
							<body>
							  <div class="container">
							    <h1>Информация о вашем заказе № {order.id}</h1>
							    <div class="total">По вашей просьбе срок хранения заказа был продлен. \n Новый срок хранения заказа до: {order.date_order_renewal_end_date.date()}</div>
							      <br/>
							    <div>Спасибо, что вы выбрали наш магазин!</div>
							  </div>
							</body>
							</html>
							"""
		msg.attach(MIMEText(html, "html"))

		# Отправка письма
		smtp_server.sendmail("qweq95346@gmail.com", user, msg.as_string())

		# Закрытие соединения
		smtp_server.quit()
		return Response({'message': 'Order edit status successfully'}, status=status.HTTP_200_OK)
	else:
		return Response({'message': 'Order edit status not successfully'}, status=status.HTTP_400_BAD_REQUEST)
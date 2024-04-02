from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SignupForm
from .models import User


from .serializers import UserSerializer
from basket.models import Basket


@api_view(['GET'])
def me(request):
	return JsonResponse({
		'id': request.user.id,
		'name': request.user.name,
		'email': request.user.email,

	})

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
	data = request.data
	message = 'success'

	form = SignupForm({
		'email': data.get('email'),
		'name': data.get('name'),
		'password1': data.get('password1'),
		'password2': data.get('password2'),
	})

	if form.is_valid():
		form.save()
		basket = Basket.objects.create(user=User.objects.get(email=form.cleaned_data['email']))
	else:
		message = form.errors.as_json()

	print(message)
	return JsonResponse({'message': message})

@api_view(['GET'])
def profile(request, id):
    user = User.objects.get(id=id)

    return JsonResponse({
        'user': UserSerializer(user).data}, safe=False)
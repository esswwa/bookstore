from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes


from .forms import BookForm
from .models import Book, Author, Published, AdditionalGenre, Genre
from .serializers import BookSerializer


@api_view(['GET'])
def book_list(request):
    # user_ids = [request.user.id]
    #
    # for user in request.user.friends.all():
    #     user_ids.append(user.id)

    books = Book.objects.get()

    serializer = BookSerializer(books, many=True)

    return JsonResponse(serializer.data, safe=False)
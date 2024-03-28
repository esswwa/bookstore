from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/', include('account.urls')),
    path('api/book/', include('book.urls')),
    path('api/basket/', include('basket.urls')),
    path('api/favourite/', include('favourite.urls')),
    path('api/order/', include('order.urls')),
    path('api/review/', include('review.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('address', include('address.urls')),
    path('masters', include('masters.urls')),
    path('registers', include('registers.urls')),
    path('schedules', include('schedules.urls')),
    path('days_off', include('days_off.urls')),
    path('categories', include('categories.urls')),
    path('services', include('services.urls')),
    path('history', include('history.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

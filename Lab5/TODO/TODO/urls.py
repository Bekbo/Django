from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('auth/', include('auth_.urls')),
    path('admin/', admin.site.urls),
]

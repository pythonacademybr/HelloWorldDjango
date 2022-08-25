from django.urls.conf import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('erp.urls', namespace='erp')),

    path('admin/', admin.site.urls),
]

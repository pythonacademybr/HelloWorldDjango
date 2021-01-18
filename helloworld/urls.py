from django.urls.conf import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('website.urls', namespace='website')),

    path('admin/', admin.site.urls),
]

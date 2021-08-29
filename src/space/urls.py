from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


# API router.
router = routers.DefaultRouter()

urlpatterns = [
    # Admin.
    path('admin/', admin.site.urls),
    # Rest API.
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]

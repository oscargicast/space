from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from field_worker.views import FieldWorkerViewSet


# API router.
router = routers.DefaultRouter()

router.register("field-workers", FieldWorkerViewSet)

urlpatterns = [
    # Admin.
    path('admin/', admin.site.urls),
    # Rest API.
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]

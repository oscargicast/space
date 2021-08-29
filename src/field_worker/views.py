from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from .models import FieldWorker
from .serializers import FieldWorkerSerializer


class FieldWorkerViewSet(viewsets.ModelViewSet):
    queryset = FieldWorker.objects.all()
    serializer_class = FieldWorkerSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = "__all__"
    ordering = ["created"]
    filterset_fields = ("function")

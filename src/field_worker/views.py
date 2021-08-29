from rest_framework import viewsets
from .models import FieldWorker
from .serializers import FieldWorkerSerializer


class FieldWorkerViewSet(viewsets.ModelViewSet):
    queryset = FieldWorker.objects.all()
    serializer_class = FieldWorkerSerializer

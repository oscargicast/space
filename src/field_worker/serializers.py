from rest_framework import serializers
from .models import FieldWorker


class FieldWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldWorker
        fields = "__all__"

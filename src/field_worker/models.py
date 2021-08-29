import uuid
from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel


class FieldWorker(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    FUNCTIONS = Choices("HARVEST", "PRUNING", "SCOUTING", "OTHER")
    function = models.CharField(
        choices=FUNCTIONS,
        default=FUNCTIONS.OTHER,
        max_length=15,
    )

    def __str__(self):
        return f"{self.id}"

    class Meta:
        db_table = "field_worker"

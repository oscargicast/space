from django.contrib import admin
from .models import FieldWorker


@admin.register(FieldWorker)
class FieldWorkerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "function",
        "created",
    )
    list_filter = (
        "function",
    )
    search_fields = (
        "first_name",
        "last_name",
    )

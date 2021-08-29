import pytest
from rest_framework.test import APIClient

from django.contrib.auth.models import User


@pytest.fixture
def user():
    return User.objects.create_user(
        "oscar",
        "oscar.gi.cast@gmail.com",
        "password",
    )

@pytest.fixture
def api_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client



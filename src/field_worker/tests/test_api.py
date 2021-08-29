import factory
import json
import pytest
from field_worker.models import FieldWorker
from hamcrest import assert_that, has_entries, equal_to
from model_bakery import baker


pytestmark = pytest.mark.django_db


class TestCurrencyEndpoints:

    endpoint = "/api/v1/field-workers/"

    def test_create(self, api_client):
        field_worker = baker.prepare(FieldWorker) 
        expected_json = {
            "first_name": field_worker.first_name,
            "last_name": field_worker.last_name,
            "function": field_worker.function,
        }
        response = api_client.post(
            self.endpoint,
            data=expected_json,
            format="json"
        )
        assert_that(response.status_code, equal_to(201))
        assert_that(response.json(), has_entries(expected_json))

    def test_list(self, api_client):
        baker.make(FieldWorker, _quantity=3)
        response = api_client.get(self.endpoint)
        assert_that(response.status_code, equal_to(200))
        assert_that(response.json().get("count"), equal_to(3))

    def test_partial_update(self, api_client):
        field_to_update = "last_name"
        field_worker = baker.make(FieldWorker) 
        url = f"{self.endpoint}{field_worker.id}/"
        response = api_client.patch(
            url,
            {field_to_update: "new last name"},
            format='json'
        )
        assert_that(response.status_code, equal_to(200))
        assert_that(response.json()[field_to_update], equal_to("new last name"))

    def test_delete(self, api_client):
        field_worker = baker.make(FieldWorker) 
        url = f"{self.endpoint}{field_worker.id}/"
        response = api_client.delete(url)
        assert_that(response.status_code, equal_to(204))
        assert_that(FieldWorker.objects.all().count(), equal_to(0))

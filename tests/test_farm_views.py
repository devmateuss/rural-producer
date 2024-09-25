import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from farm.models import Crop, Farm, Producer


@pytest.fixture
def producer():
    return Producer.objects.create(document="12345678901", name="John Doe")


@pytest.fixture
def farm_mock(producer):
    return Farm.objects.create(
        producer=producer,
        name="Farm 1",
        city="City 1",
        state="State 1",
        total_area=100.0,
        agricultural_area=60.0,
        vegetation_area=40.0,
    )


@pytest.fixture
def crop_mock():
    return Crop.objects.create(name="AÇUCAR")


@pytest.fixture
def farm_data(producer, crop_mock):
    return {
        "name": "Farm 1",
        "city": "City 1",
        "state": "State 1",
        "total_area": 100.0,
        "agricultural_area": 60.0,
        "vegetation_area": 40.0,
        "planted_crops": [crop_mock.id],
        "producer": producer.id,
    }


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_create_farm(api_client, farm_data):
    url = reverse("farm-list")
    response = api_client.post(url, farm_data, format="json")

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_get_farm_list(api_client, farm_mock):
    url = reverse("farm-list")
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
    assert farm_mock.id == response.data[0].get("id")


@pytest.mark.django_db
def test_update_farm(api_client, farm_data, farm_mock):
    url = reverse("farm-detail", args=[farm_mock.id])
    farm_data["name"] = "Farm Updated"

    response = api_client.put(url, farm_data, format="json")
    farm_mock.refresh_from_db()

    assert response.status_code == status.HTTP_200_OK
    assert farm_mock.name == "Farm Updated"


@pytest.mark.django_db
def test_delete_farm(api_client, farm_mock):
    url = reverse("farm-detail", args=[farm_mock.id])

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Farm.objects.count() == 0

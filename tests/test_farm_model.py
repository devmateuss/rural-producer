from unittest.mock import patch

import pytest
from django.core.exceptions import ValidationError

from farm.models import Farm
from producer.models import Producer


@pytest.mark.django_db
class TestFarmModel:

    @patch("farm.models.Farm.save")
    def test_create_farm(self, mock_save):
        producer = Producer(document="12345678901", name="John Doe")
        farm = Farm(
            name="Farm Test",
            city="Fortaleza",
            state="Ceará",
            total_area=100.0,
            agricultural_area=70.0,
            vegetation_area=30.0,
            producer=producer,
        )
        farm.save()
        mock_save.assert_called_once()

    @patch("farm.models.Farm.full_clean")
    def test_area_validation(self, mock_full_clean):
        mock_full_clean.side_effect = ValidationError("Invalid areas")
        producer = Producer(document="12345678901", name="John Doe")
        farm = Farm(
            name="Invalid Farm",
            city="Fortaleza",
            state="Ceará",
            total_area=50.0,
            agricultural_area=30.0,
            vegetation_area=30.0,
            producer=producer,
        )
        with pytest.raises(ValidationError):
            farm.full_clean()

    @patch("farm.models.Farm.save")
    def test_update_farm(self, mock_save):
        producer = Producer(document="12345678901", name="John Doe")
        farm = Farm(
            name="Farm Test",
            city="Fortaleza",
            state="Ceará",
            total_area=100.0,
            agricultural_area=70.0,
            vegetation_area=30.0,
            producer=producer,
        )
        farm.name = "Updated Farm Name"
        farm.save()
        mock_save.assert_called()

    @patch("farm.models.Farm.delete")
    def test_delete_farm(self, mock_delete):
        producer = Producer(document="12345678901", name="John Doe")
        farm = Farm(
            name="Farm Test",
            city="Fortaleza",
            state="Ceará",
            total_area=100.0,
            agricultural_area=70.0,
            vegetation_area=30.0,
            producer=producer,
        )
        farm.delete()
        mock_delete.assert_called_once()

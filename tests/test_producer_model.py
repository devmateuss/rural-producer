from unittest.mock import patch

import pytest
from django.core.exceptions import ValidationError

from producer.models import Producer


@pytest.mark.django_db
class TestProducerModel:

    @patch("producer.models.Producer.save")
    def test_create_producer(self, mock_save):
        producer = Producer(document="12345678901", name="John Doe")
        producer.save()
        mock_save.assert_called_once()

    @patch("producer.models.Producer.full_clean")
    def test_create_invalid_cpf(self, mock_full_clean):
        mock_full_clean.side_effect = ValidationError("Invalid CPF")
        producer = Producer(document="123", name="Invalid CPF")
        with pytest.raises(ValidationError):
            producer.full_clean()

    @patch("producer.models.Producer.full_clean")
    def test_create_invalid_cnpj(self, mock_full_clean):
        mock_full_clean.side_effect = ValidationError("Invalid CNPJ")
        producer = Producer(document="12345678901234", name="Invalid CNPJ")
        with pytest.raises(ValidationError):
            producer.full_clean()

    @patch("producer.models.Producer.save")
    def test_update_producer(self, mock_save):
        producer = Producer(document="12345678901", name="John Doe")
        producer.name = "Updated Name"
        producer.save()
        mock_save.assert_called()

    @patch("producer.models.Producer.delete")
    def test_delete_producer(self, mock_delete):
        producer = Producer(document="12345678901", name="John Doe")
        producer.delete()
        mock_delete.assert_called_once()

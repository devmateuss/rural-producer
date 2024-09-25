from django.test import TestCase

from farm.models import Crop, Farm
from producer.models import Producer
from producer.services.producer_farm_service import ProducerFarmService


class ProducerFarmServiceTest(TestCase):

    def setUp(self):
        crop_instance = Crop
        self.crop1 = crop_instance.objects.create(name="Milho")
        self.crop2 = crop_instance.objects.create(name="Soja")

        self.producer_data = {"document": "12345678901", "name": "Produtor Teste"}

        self.farm_data = {
            "name": "Fazenda Teste",
            "city": "Fortaleza",
            "state": "CE",
            "total_area": 1000.0,
            "agricultural_area": 500.0,
            "vegetation_area": 400.0,
            "planted_crops": [self.crop1.id, self.crop2.id],
        }

    def test_create_producer_farm(self):
        data = {"producer": self.producer_data, "farm": self.farm_data}
        result = ProducerFarmService.create_producer_farm(data)

        producer = result["producer"]
        farm = result["farm"]

        self.assertIsInstance(producer, Producer)
        self.assertIsInstance(farm, Farm)
        self.assertEqual(producer.name, "Produtor Teste")
        self.assertEqual(farm.name, "Fazenda Teste")
        self.assertEqual(list(farm.planted_crops.all()), [self.crop1, self.crop2])

    def test_list_producer_farm(self):
        ProducerFarmService.create_producer_farm(
            {"producer": self.producer_data, "farm": self.farm_data}
        )

        result = ProducerFarmService.list_producer_farm()
        self.assertEqual(result.count(), 1)

        farm = result.first()
        self.assertEqual(farm.name, "Fazenda Teste")
        self.assertEqual(farm.producer.name, "Produtor Teste")

    def test_update_producer_farm(self):
        result = ProducerFarmService.create_producer_farm(
            {"producer": self.producer_data, "farm": self.farm_data}
        )
        producer_id = result["producer"].id

        updated_data = {
            "producer": {"name": "Produtor Atualizado"},
            "farm": {"name": "Fazenda Atualizada", "planted_crops": [self.crop1.id]},
        }

        result = ProducerFarmService.update_producer_farm(producer_id, updated_data)

        producer = result["producer"]
        farm = result["farm"]

        self.assertEqual(producer.name, "Produtor Atualizado")
        self.assertEqual(farm.name, "Fazenda Atualizada")
        self.assertEqual(list(farm.planted_crops.all()), [self.crop1])

    def test_delete_producer_farm(self):
        producer_instance = Producer
        farm_instance = Farm
        result = ProducerFarmService.create_producer_farm(
            {"producer": self.producer_data, "farm": self.farm_data}
        )
        producer_id = result["producer"].id
        self.assertEqual(producer_instance.objects.count(), 1)
        self.assertEqual(farm_instance.objects.count(), 1)

        delete_result = ProducerFarmService.delete_producer_farm(producer_id)
        self.assertEqual(
            delete_result["message"], "Produtor e fazenda excluídos com sucesso."
        )

        self.assertEqual(producer_instance.objects.count(), 0)
        self.assertEqual(farm_instance.objects.count(), 0)

    def test_get_producer_farm(self):
        result = ProducerFarmService.create_producer_farm(
            {"producer": self.producer_data, "farm": self.farm_data}
        )
        producer_id = result["producer"].id

        result = ProducerFarmService.get_producer_farm(producer_id)

        producer = result["producer"]
        farm = result["farm"]

        self.assertEqual(producer.name, "Produtor Teste")
        self.assertEqual(farm.name, "Fazenda Teste")

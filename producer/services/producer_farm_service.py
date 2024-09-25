# services/producer_farm_service.py

from django.core.exceptions import ValidationError
from django.db import transaction

from farm.models import Farm
from producer.models import Producer


class ProducerFarmService:

    @staticmethod
    def list_producer_farm():
        try:
            return (
                Farm.objects.all()
                .select_related("producer")
                .prefetch_related("planted_crops")
            )
        except Exception as e:
            raise ValidationError(f"Erro ao listar produtor e fazenda: {str(e)}")

    @staticmethod
    @transaction.atomic
    def create_producer_farm(data):
        try:
            producer_data = data.get("producer")
            farm_data = data.get("farm")
            planted_crops_data = farm_data.pop("planted_crops", [])

            producer = Producer.objects.create(**producer_data)
            farm = Farm.objects.create(producer=producer, **farm_data)
            farm.planted_crops.set(planted_crops_data)

            return {"producer": producer, "farm": farm}
        except Exception as e:
            raise ValidationError(f"Erro ao criar produtor e fazenda: {str(e)}")

    @staticmethod
    @transaction.atomic
    def update_producer_farm(producer_id, data):
        try:
            producer = Producer.objects.get(id=producer_id)
            producer_data = data.get("producer")
            farm_data = data.get("farm")

            for field, value in producer_data.items():
                setattr(producer, field, value)
            producer.save()

            farm = Farm.objects.filter(producer=producer).first()

            for field, value in farm_data.items():
                if field == "planted_crops":
                    farm.planted_crops.set(value)
                else:
                    setattr(farm, field, value)
            farm.save()

            return {"producer": producer, "farm": farm}
        except Producer.DoesNotExist:
            raise ValidationError("Produtor não encontrado.")
        except Exception as e:
            raise ValidationError(f"Erro ao atualizar produtor e fazenda: {str(e)}")

    @staticmethod
    @transaction.atomic
    def delete_producer_farm(producer_id):
        try:
            producer = Producer.objects.get(id=producer_id)
            Farm.objects.filter(producer=producer).delete()
            producer.delete()
            return {"message": "Produtor e fazenda excluídos com sucesso."}
        except Producer.DoesNotExist:
            raise ValidationError("Produtor não encontrado.")

    @staticmethod
    def get_producer_farm(producer_id):
        try:
            producer = Producer.objects.get(id=producer_id)
            farm = Farm.objects.filter(producer=producer).first()
            return {"producer": producer, "farm": farm}
        except Producer.DoesNotExist:
            raise ValidationError("Produtor não encontrado.")

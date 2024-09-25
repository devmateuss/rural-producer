from rest_framework import serializers

from farm.models import Farm
from farm.serializers import CropSerializer, FarmSerializer
from producer.models import Producer


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = "__all__"


class ProducerFarmSerializer(serializers.Serializer):
    producer = ProducerSerializer()
    farm = FarmSerializer()


class ProducerFarmAllSerializer(serializers.ModelSerializer):
    producer = ProducerSerializer()
    planted_crops = CropSerializer(many=True)

    class Meta:
        model = Farm
        fields = [
            "producer",
            "name",
            "city",
            "state",
            "total_area",
            "agricultural_area",
            "vegetation_area",
            "planted_crops",
        ]

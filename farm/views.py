from common.viewsets import BaseModelViewSet
from farm.models import Crop, Farm
from farm.serializers import CropSerializer, FarmSerializer


class FarmViewSet(BaseModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer


class CropViewSet(BaseModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.response import Response

from common.viewsets import BaseModelViewSet
from producer.models import Producer
from producer.serializers import (
    ProducerFarmAllSerializer,
    ProducerFarmSerializer,
    ProducerSerializer,
)
from producer.services.dashboard_service import DashboardService
from producer.services.producer_farm_service import ProducerFarmService


class ProducerViewSet(BaseModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer


class DashboardAPIView(viewsets.ViewSet):

    @swagger_auto_schema(
        operation_description="Retorna dados para o dashboard de fazendas",
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "total_farms": openapi.Schema(
                        type=openapi.TYPE_INTEGER,
                        description="Total de fazendas cadastradas",
                    ),
                    "total_area": openapi.Schema(
                        type=openapi.TYPE_NUMBER,
                        format=openapi.FORMAT_FLOAT,
                        description="Total de hectares das fazendas",
                    ),
                    "state_distribution": openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        description="Distribuição das fazendas por estado",
                        additional_properties=openapi.Schema(type=openapi.TYPE_INTEGER),
                    ),
                    "crop_distribution": openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        description="Distribuição das fazendas por cultura plantada",
                        additional_properties=openapi.Schema(type=openapi.TYPE_INTEGER),
                    ),
                    "land_usage": openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "agricultural_area": openapi.Schema(
                                type=openapi.TYPE_NUMBER,
                                format=openapi.FORMAT_FLOAT,
                                description="Área agricultável total",
                            ),
                            "vegetation_area": openapi.Schema(
                                type=openapi.TYPE_NUMBER,
                                format=openapi.FORMAT_FLOAT,
                                description="Área de vegetação total",
                            ),
                        },
                    ),
                },
            )
        },
        tags=["Dashboard"],
    )
    def list(self, _request):
        stats = DashboardService.get_farm_stats()
        return Response(stats)


class ProducerFarmViewSet(viewsets.ViewSet):
    """
    Retorna todos os produtores e sua fazenda
    """

    def list(self, _request):
        result = ProducerFarmService.list_producer_farm()
        serializer = ProducerFarmAllSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_description="Cria um novo produtor com uma fazenda associada",
        request_body=ProducerFarmSerializer,
        responses={
            status.HTTP_201_CREATED: openapi.Response(
                description="Produtor e fazenda criados com sucesso",
                schema=ProducerFarmSerializer,
            ),
            status.HTTP_400_BAD_REQUEST: "Requisição inválida",
        },
    )
    def create(self, request):
        data = request.data
        result = ProducerFarmService.create_producer_farm(data)
        serializer = ProducerFarmSerializer(result)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """
        Atualiza um produtor e sua fazenda
        """
        data = request.data
        result = ProducerFarmService.update_producer_farm(pk, data)
        serializer = ProducerFarmSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, _request, pk):
        """
        Exclui um produtor e sua fazenda
        """
        result = ProducerFarmService.delete_producer_farm(pk)
        return Response(result, status=status.HTTP_200_OK)

    def get(self, _request, pk):
        """
        Retorna os detalhes de um produtor e sua fazenda
        """
        result = ProducerFarmService.get_producer_farm(pk)
        serializer = ProducerFarmSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)

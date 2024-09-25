from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet


class BaseModelViewSet(ModelViewSet):
    """
    Classe base abstrata que gera automaticamente a documentação Swagger para ModelViewSet.
    """

    def get_create_description(self):
        return f"Cadastra um novo(a) {self.get_model_name()}."

    def get_update_description(self):
        return f"Atualiza um(a) {self.get_model_name()} existente."

    def get_destroy_description(self):
        return f"Exclui um(a) {self.get_model_name()}."

    @swagger_auto_schema(operation_description="Listagem de objetos")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Detalhes do objeto")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Criação de objeto")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Atualização de objeto")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Exclusão de objeto")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Atualiza parcialmente um objeto existente."
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    class Meta:
        abstract = True

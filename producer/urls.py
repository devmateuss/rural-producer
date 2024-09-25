from django.urls import include, path
from rest_framework import routers

from producer.views import DashboardAPIView, ProducerFarmViewSet, ProducerViewSet

router = routers.SimpleRouter()
router.register(r"producer", ProducerViewSet, basename="producer")
router.register(r"rural-producer", ProducerFarmViewSet, basename="producer-farms")
router.register(r"dashboard", DashboardAPIView, basename="dashboard")


urlpatterns = [
    path("", include(router.urls)),
]

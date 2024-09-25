from rest_framework import routers

from farm.views import CropViewSet, FarmViewSet

router = routers.DefaultRouter()
router.register(r"farm", FarmViewSet, basename="farm")
router.register(r"crop", CropViewSet)

urlpatterns = router.urls

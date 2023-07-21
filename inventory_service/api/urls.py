from rest_framework_nested import routers

from .views import InventoryViewSet
router = routers.DefaultRouter()

router.register("inventory", InventoryViewSet, basename="inventory")

urlpatterns = router.urls
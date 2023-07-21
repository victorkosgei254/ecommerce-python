from rest_framework_nested import routers

from .views import OrderViewSet
router = routers.DefaultRouter()

router.register("order", OrderViewSet, basename="order")

urlpatterns = router.urls
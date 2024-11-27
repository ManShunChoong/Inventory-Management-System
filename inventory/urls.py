from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import InventoryModelViewSet, InventoryViewSet

router = DefaultRouter()
router.register(r"api/inventory", InventoryModelViewSet)
router.register(r"inventory", InventoryViewSet, basename="inventory-viewset")

urlpatterns = router.urls

from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import InventoryAPIModelViewSet, InventoryTemplateModelViewSet

router = DefaultRouter()
router.register(r"api/inventory", InventoryAPIModelViewSet)
router.register(
    r"inventory", InventoryTemplateModelViewSet, basename="inventory-template"
)

urlpatterns = router.urls

import requests
from django.conf import settings
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet

from .forms import InventoryForm
from .models import Inventory
from .serializers import InventoryListSerializer, InventorySerializer


class InventoryModelViewSet(ReadOnlyModelViewSet):
    queryset = Inventory.objects.all()
    action_serializer_classes = {
        "list": InventoryListSerializer,
        "retrieve": InventorySerializer,
    }
    filterset_fields = ["availability"]
    search_fields = ["name", "supplier__name"]

    def get_serializer_class(self):
        return self.action_serializer_classes[self.action]


class InventoryViewSet(ViewSet):
    def list(self, request):
        url = f"{settings.BASE_URL}/api/inventory/"
        response = requests.get(url, params=request.GET)
        inventories = response.json()
        context = {"inventories": inventories, "form": InventoryForm()}

        return render(request, "inventory_list.html", context)

    def retrieve(self, request, pk=None):
        response = requests.get(url=f"{settings.BASE_URL}/api/inventory/{pk}/")
        inventory = response.json()

        return render(request, "inventory_detail.html", {"inventory": inventory})

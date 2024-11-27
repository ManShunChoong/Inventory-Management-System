import requests
from django.shortcuts import render
from django.views import View
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
        search = request.GET.get("search", "")
        availability = request.GET.get("availability")
        url = f"http://127.0.0.1:8000/api/inventory/?search={search}&availability={availability}"

        response = requests.get(url)
        inventories = response.json()
        context = {"inventories": inventories, "form": InventoryForm()}

        return render(request, "inventory_list.html", context)

    def retrieve(self, request, pk=None):
        url = f"http://127.0.0.1:8000/api/inventory/{pk}/"
        response = requests.get(url)
        inventory = response.json()

        return render(request, "inventory_detail.html", {"inventory": inventory})

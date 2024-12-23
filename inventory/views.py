from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.request import Request
from rest_framework.serializers import Serializer
from rest_framework.viewsets import GenericViewSet

from .forms import InventoryForm
from .models import Inventory
from .serializers import InventoryDetailSerializer, InventoryListSerializer


class BaseInventoryModelViewSet(GenericViewSet):
    queryset = Inventory.objects
    action_serializer_classes = {
        "retrieve": InventoryDetailSerializer,
        "list": InventoryListSerializer,
    }
    filterset_fields = ["name", "availability"]
    search_fields = ["name", "supplier_name"]

    def get_queryset(self) -> QuerySet:
        return self.queryset.select_related("supplier")

    def get_serializer_class(self) -> Serializer:
        return self.action_serializer_classes[self.action]

    def retrieve(self, request: Request, *args, **kwargs) -> HttpResponse:
        raise NotImplementedError(
            f"'{self.__class__.__name__}.retrieve()' must be implemented."
        )

    def list(self, request: Request, *args, **kwargs) -> HttpResponse:
        raise NotImplementedError(
            f"'{self.__class__.__name__}.list()' must be implemented."
        )


class InventoryAPIModelViewSet(
    RetrieveModelMixin, ListModelMixin, BaseInventoryModelViewSet
):
    pass


class InventoryTemplateModelViewSet(BaseInventoryModelViewSet):
    def retrieve(self, request: Request, *args, **kwargs) -> HttpResponse:
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        context = {"inventory": serializer.data}
        return render(request, "inventory_detail.html", context)

    def list(self, request: Request, *args, **kwargs) -> HttpResponse:
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        context = {"inventories": serializer.data, "form": InventoryForm()}
        return render(request, "inventory_list.html", context)

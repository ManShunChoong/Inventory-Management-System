from rest_framework.serializers import CharField, ModelSerializer

from .models import Inventory


class InventoryDetailSerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"
        depth = 1


class InventoryListSerializer(ModelSerializer):
    supplier_name = CharField(read_only=True)

    class Meta:
        model = Inventory
        fields = ["id", "name", "supplier_name", "availability"]

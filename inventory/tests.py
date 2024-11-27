from django.test import TestCase
from django.urls import reverse

from .models import Inventory, Supplier


class InventoryModelTestCase(TestCase):
    def test_inventory_list(self):
        response = self.client.get(reverse("inventory-list"))
        self.assertEqual(response.status_code, 200)

    def test_inventory_detail(self):
        supplier = Supplier.objects.create(name="Test Supplier")
        inventory = Inventory.objects.create(
            name="Test Inventory", stock=10, supplier=supplier
        )
        response = self.client.get(reverse("inventory-detail", args=[inventory.id]))
        self.assertEqual(response.status_code, 200)


class InventoryViewSetTestCase(TestCase):
    def test_inventory_list(self):
        response = self.client.get(reverse("inventory-viewset-list"))
        self.assertEqual(response.status_code, 200)

    def test_inventory_detail(self):
        supplier = Supplier.objects.create(name="Test Supplier")
        inventory = Inventory.objects.create(
            name="Test Inventory", stock=10, supplier=supplier
        )
        response = self.client.get(
            reverse("inventory-viewset-detail", args=[inventory.id])
        )
        self.assertEqual(response.status_code, 200)

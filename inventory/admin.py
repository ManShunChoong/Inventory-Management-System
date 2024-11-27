from django.contrib.admin import site

from .models import Inventory, Supplier

site.register(Supplier)
site.register(Inventory)

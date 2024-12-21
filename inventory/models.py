from django.db.models import (
    PROTECT,
    BooleanField,
    CharField,
    ForeignKey,
    Model,
    PositiveIntegerField,
    TextField,
    UniqueConstraint,
)


class Supplier(Model):
    name = CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return f"{self.pk} - {self.name}"


class Inventory(Model):
    name = CharField(max_length=50)
    description = CharField(max_length=100, null=True)
    note = TextField(null=True)
    stock = PositiveIntegerField(default=0)
    availability = BooleanField(default=True)
    supplier = ForeignKey("Supplier", on_delete=PROTECT)

    class Meta:
        constraints = [
            UniqueConstraint(fields=["name", "supplier"], name="unique_name_supplier")
        ]
        verbose_name_plural = "Inventories"

    def __str__(self) -> str:
        return f"{self.pk} - {self.name}"

from django.forms import CharField, ChoiceField, Form


class InventoryForm(Form):
    search = CharField(max_length=100, required=False)
    availability = ChoiceField(
        choices=[(None, "---------"), (True, "Available"), (False, "Not Available")],
        required=False,
    )

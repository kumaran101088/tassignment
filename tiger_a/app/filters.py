from django_filters import FilterSet
from .models import Inventory

class InventoryFilter(FilterSet):

    class Meta:
        model = Inventory
        fields = {
            'store' : ['iexact'],
            'sku' : ['iexact'],
            'price' : ['lte', 'gte'],
            'product' : ['icontains'],
            'date' : ['exact']
        }
# required models in serilizer page
from .models import (
    CoffeeMachines,
    CoffeePods
)
# required serializers
from rest_framework import (
    serializers
)


# make CoffeeMachines serializer and get data model in it
class CoffeeMachinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeMachines
        fields = ['SKU', 'model_type', 'product_type', 'water_line_compatible']


# make CoffeePods serializer and get data model in it
class CoffeePodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeePods
        fields = ['SKU', 'product_type', 'coffee_flavor', 'pack_size']

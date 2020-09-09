# required models in serilizer page
from .models import (
    CoffeeMachines,
    CoffeePods
)
# required serializers
from rest_framework import (
    serializers
)


# make CoffeeMachines serializer and get all data model in it
class CoffeeMachinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeMachines
        fields = '__all__'


# make CoffeePods serializer and get all data model in it
class CoffeePodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeePods
        fields = '__all__'

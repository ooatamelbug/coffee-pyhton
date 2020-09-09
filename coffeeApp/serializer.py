from .models import (
    CoffeeMachines,
    CoffeePods
)
from rest_framework import (
    serializers


class CoffeeMachinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeMachines
        fields = '__all__'


class CoffeePodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeePods
        fields = '__all__'

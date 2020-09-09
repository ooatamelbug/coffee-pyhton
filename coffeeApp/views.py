# required serializer
from .serializer import (
    CoffeeMachinesSerializer,
    CoffeePodsSerializer
)


# required rest_framework generics
from rest_framework.generics import (
    ListAPIView
)


# required models
from .models import (
    CoffeeMachines,
    CoffeePods
)

# Create your views here.


class CoffeeMachines(ListAPIView):
    queryset = CoffeeMachines.objects.all()
    serializer_class = CoffeeMachinesSerializer


class CoffeePods(ListAPIView):
    queryset = CoffeePods.objects.all()
    serializer_class = CoffeePodsSerializer

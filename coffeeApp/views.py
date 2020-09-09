rom .serializer import (
    CoffeeMachinesSerializer,
    CoffeePodsSerializer,
)


from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)


from .models import (
    CoffeeMachines,
    CoffeePods
)
# Create your views here.

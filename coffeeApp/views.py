# required serializer
from .serializer import (
    CoffeeMachinesSerializer,
    CoffeePodsSerializer
)
# required api_view
from rest_framework.decorators import api_view
# required models
from .models import (
    CoffeeMachines,
    CoffeePods
)
# required Response
from rest_framework.response import Response


# Create coffeemachines views function.
@api_view(['GET'])
def coffeemachines(request):
    if request.GET.get("model_type"):
        filterdata = '%' + request.GET.get("model_type") + '%'
        queryset = CoffeeMachines.objects.filter(model_type__contains=filterdata)
    elif request.GET.get("product_type"):
        filterdata = '%' + request.GET.get("product_type") + '%'
        queryset = CoffeeMachines.objects.filter(product_type__contains=filterdata)
    elif request.GET.get("water_line_compatible"):
        filterdata = '%' + request.GET.get("water_line_compatible") + '%'
        queryset = CoffeeMachines.objects.filter(water_line_compatible__contains=filterdata)
    else:
        queryset = CoffeeMachines.objects.all()
    serializer = CoffeeMachinesSerializer(queryset, many=True)
    return Response(serializer.data)


# Create coffeepods views function.
@api_view(['GET'])
def coffeepods(request):
    if request.GET.get("product_type"):
        filterdata = '%' + request.GET.get("product_type") + '%'
        queryset = CoffeePods.objects.filter(product_type__contains=filterdata)
    elif request.GET.get("coffee_flavor"):
        filterdata = '%' + request.GET.get("coffee_flavor") + '%'
        queryset = CoffeePods.objects.filter(coffee_flavor__contains=filterdata)
    elif request.GET.get("pack_size"):
        filterdata = '%' + request.GET.get("pack_size") + '%'
        queryset = CoffeePods.objects.filter(pack_size__contains=filterdata)
    else:
        queryset = CoffeePods.objects.all()
    serializer = CoffeePodsSerializer(queryset, many=True)
    return Response(serializer.data)


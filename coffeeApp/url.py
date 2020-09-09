from django.urls import path
from .views import (
    CoffeeMachines,
    CoffeePods
)

urlpatterns = [
    path('machines/', CoffeeMachines.as_view(), name='machines'),
    path('pods/', CoffeePods.as_view(), name='pods'),
]

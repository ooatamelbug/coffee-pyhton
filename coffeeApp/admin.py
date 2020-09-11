from django.contrib import admin

# required models
from .models import (
    CoffeeMachines,
    CoffeePods
)

# Register CoffeeMachines,CoffeePods models in admin.
admin.site.register(CoffeeMachines)
admin.site.register(CoffeePods)

from django.urls import path
from .views import (
    coffeemachines,
    coffeepods
)
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('machines/', coffeemachines, name='machines'),
    path('pods/', coffeepods, name='pods'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

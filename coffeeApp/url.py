# required path
from django.urls import path
# required views function
from .views import (
    coffeemachines,
    coffeepods
)
# required format_suffix_patterns
from rest_framework.urlpatterns import format_suffix_patterns


# Create urlpatterns.
urlpatterns = [
    path('machines/', coffeemachines, name='machines'),
    path('pods/', coffeepods, name='pods'),
]


# format urlpatterns.
urlpatterns = format_suffix_patterns(urlpatterns)

from djongo import models

# Create your models here.


class CoffeeMachines(models.Model):
    _id = models.ObjectIdField()
    SKU = models.CharField(max_length=255)
    model_model = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    water_line_compatible = models.BooleanField()


class CoffeePods(models.Model):
    _id = models.ObjectIdField()
    SKU = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    coffee_flavor = models.CharField(max_length=255)
    pack_size = models.CharField(max_length=255)


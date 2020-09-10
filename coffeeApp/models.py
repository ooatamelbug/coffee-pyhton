from djongo import models


# Create CoffeeMachines models.
class CoffeeMachines(models.Model):
    _id = models.ObjectIdField()
    SKU = models.CharField(max_length=255)
    model_type = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    water_line_compatible = models.BooleanField()

    def __str__(self):
        return self.SKU + ', ' + self.product_type + ', ' + self.model_type + ',' + self.water_line_compatible


# Create CoffeePods models.
class CoffeePods(models.Model):
    _id = models.ObjectIdField()
    SKU = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    coffee_flavor = models.CharField(max_length=255)
    pack_size = models.CharField(max_length=255)

    def __str__(self):
        return self.SKU + ', ' + self.product_type + ', ' + self.coffee_flavor + ',' + self.pack_size


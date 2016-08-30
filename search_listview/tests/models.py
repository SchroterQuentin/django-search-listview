from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=100, verbose_name="Provider's name")

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Brand's name")

    provider = models.ManyToManyField(Provider, verbose_name="Brand's provider")

    def __str__(self):
        return self.name

class ModelDevice(models.Model):
    name = models.CharField(max_length=100, verbose_name="Model's name")

    brand = models.ForeignKey(Brand, verbose_name="Model's brand")

    def __str__(self):
        return self.name

class Device(models.Model):
    inventory_number = models.PositiveIntegerField()

    model_device = models.ForeignKey(ModelDevice, verbose_name="Device's model'")

    def __str__(self):
        return str(self.inventory_number)



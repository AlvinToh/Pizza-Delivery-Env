from django.db import models


class PizzaModel(models.Model):
    name = models.CharField(max_length=10)
    price = models.CharField(max_length=10)

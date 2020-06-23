from django.db import models


class PizzaModel(models.Model):
    name = models.CharField(max_length=10)
    price = models.CharField(max_length=10)


class CustomerModel(models.Model):
    userid = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)

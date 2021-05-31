# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Country(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100, null=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    code = models.CharField(max_length=5, blank=False, null=False)

class State(models.Model):
    name = models.ForeignKey(Country, on_delete=models.CASCADE)

class Address(models.Model):
    name = models.ForeignKey(State, on_delete=models.CASCADE)
    house = models.CharField(max_length=255)
    road = models.CharField(max_length=12)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Location(models.Model):
    country = models.CharField(max_length=70, default=None)

    def __str__(self):
        return self.country


class PersonDetail(models.Model):
    person_img = models.ImageField(default=None, null=True, blank=True)
    First_name = models.CharField(max_length=250)
    Last_name = models.CharField(max_length=250)
    organization = models.CharField(max_length=70)
    designation = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    country = models.ForeignKey(Location, default=None)
    state = models.CharField(max_length=50, default=None)
    city = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.First_name

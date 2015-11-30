#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmenta
# @Date:   2015-11-17 12:37:09
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-28 14:43:05
from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides selfupdating
    ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Countries(models.Model):
    id_countries = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    iso_alpha2 = models.CharField(max_length=2, blank=True, null=True)
    iso_alpha3 = models.CharField(max_length=3, blank=True, null=True)
    iso_numeric = models.IntegerField(blank=True, null=True)
    currency_code = models.CharField(max_length=3, blank=True, null=True)
    currency_name = models.CharField(max_length=32, blank=True, null=True)
    currrency_symbol = models.CharField(max_length=3, blank=True, null=True)
    flag = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'

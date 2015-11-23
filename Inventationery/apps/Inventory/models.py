#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:10:36
# @Last Modified by:   harmenta
# @Last Modified time: 2015-11-23 10:54:27
from django.db import models
from Inventationery.apps.Vendor.models import VendorModel
from Inventationery.core.models import TimeStampedModel


# Class: Model for Inventory item
# ----------------------------------------------------------------------------
class InventModel(TimeStampedModel):

    ItemId = models.CharField(max_length=20, unique=True)
    ItemName = models.CharField(max_length=50)
    Description = models.CharField(max_length=100, blank=True, null=True)
    UnitId = models.CharField(max_length=20)
    PrimaryVendor = models.ForeignKey(
        VendorModel, default=None, blank=True, null=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    VendorPrice = models.DecimalField(max_digits=10, decimal_places=2)
    ItemImage = models.ImageField(
        upload_to="ItemTable/", default=None, blank=True, null=True)

    def __unicode__(self):
        return "{0}".format(self.ItemId)

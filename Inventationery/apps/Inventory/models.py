#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:10:36
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-06 17:19:25
from django.db import models
from Inventationery.apps.Vendor.models import VendorModel
from Inventationery.core.models import TimeStampedModel


# Class: Model for Inventory item
# ----------------------------------------------------------------------------
class ItemModel(TimeStampedModel):

    INSTOCK = 'INS'
    OFFSTOCK = 'OFS'
    SERVICE = 'SER'

    ItemTypes = (
        (INSTOCK, 'En stock'),
        (OFFSTOCK, 'Fuera de stock'),
        (SERVICE, 'Servicio'),
    )

    ItemId = models.CharField(max_length=20, unique=True)
    ItemType = models.CharField(
        max_length=20, null=True, blank=True, choices=ItemTypes)
    ItemName = models.CharField(max_length=50)
    Description = models.TextField(max_length=100, blank=True, null=True)
    UnitId = models.CharField(max_length=20)
    PrimaryVendor = models.ForeignKey(
        VendorModel, default=None, blank=True, null=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    VendorPrice = models.DecimalField(max_digits=10, decimal_places=2)
    ItemImage = models.ImageField(
        upload_to="ItemTable/", default=None, blank=True, null=True)

    def __unicode__(self):
        return "{0}".format(self.ItemId)


class LocationModel(TimeStampedModel):
    LocationName = models.CharField(max_length=50, default='Default')

    def __unicode__(self):
        return "{0}".format(self.LocationName)


class InventoryModel(TimeStampedModel):

    Item = models.ForeignKey(ItemModel,
                             default=None,
                             related_name='Item',
                             null=True,
                             blank=True)
    Location = models.ForeignKey(
        LocationModel, null=True, blank=True, related_name='Location')
    Qty = models.IntegerField(default=0, null=True)

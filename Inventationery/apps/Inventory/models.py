#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:10:36
# @Last Modified by:   harmenta
# @Last Modified time: 2015-12-30 17:25:51
from django.db.models import Q
from django.db import models
from django.contrib.auth.models import User
from Inventationery.apps.Vendor.models import VendorModel
from Inventationery.core.models import TimeStampedModel


# Class: Model for prduct item
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
    PrimaryVendor = models.ForeignKey(
        VendorModel, default=None, blank=True, null=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    # VendorPrice = models.DecimalField(max_digits=10, decimal_places=2)
    ItemImage = models.ImageField(
        upload_to="ItemTable", default=None, blank=True, null=True)

    def __unicode__(self):
        return "{0}".format(self.ItemId)

    # Get sales unit value
    def getSalesUnit(self):
        try:
            return EcoResProductModel.objects.filter(Item=self).get().SalesUnit
        except:
            return ''

    # Get vendor price
    def getPurchUnit(self):
        try:
            return EcoResProductModel.objects.filter(Item=self).get().PurchUnit
        except:
            return ''

    # Get vendor price
    def getPurchPrice(self):
        try:
            return ItemVendorModel.objects.filter(
                Q(Item=self) & Q(Vendor=self.PrimaryVendor)).get().VendorPrice
        except:
            return ''

    # Verify if item is in stock
    def CanDelete(self):
        InventoryItem = InventoryModel.objects.filter(Item=self)
        if InventoryItem:
            return False
        else:
            return True

    # Get item total in stock
    def GetInventoryTotalItems(self):
        total = 0
        items = InventoryModel.objects.filter(Item=self)
        for item in items:
            total += item.Qty
        return total


# Class: Model for product vendors
# ----------------------------------------------------------------------------
class ItemVendorModel(TimeStampedModel):
    Item = models.ForeignKey(ItemModel, default=None, blank=True, null=True)
    Vendor = models.ForeignKey(
        VendorModel, default=None, blank=True, null=True)
    VendorItemId = models.CharField(max_length=20, blank=True, null=True)
    VendorPrice = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)


# Class: Model for pruduct locations
# ----------------------------------------------------------------------------
class LocationModel(TimeStampedModel):
    LocationName = models.CharField(
        max_length=50, default='Default', unique=True)

    def __unicode__(self):
        return "{0}".format(self.LocationName)

    def GetTotalItems(self):
        qty = 0
        try:
            Inventory = InventoryModel.objects.filter(Location=self).get()
            for inventory in Inventory:
                qty += inventory.Qty
        except:
            qty = 0

        return qty


# Class: Model for product vendors
# ----------------------------------------------------------------------------
class EcoResProductModel(TimeStampedModel):
    Item = models.OneToOneField(ItemModel, default=None, blank=True, null=True)
    BarCode = models.CharField(
        max_length=50, default=None, blank=True, null=True)
    DefaultLocation = models.ForeignKey(
        LocationModel, null=True, blank=True, related_name='DefaultLocation')
    LastVendor = models.ForeignKey(
        VendorModel, default=None, blank=True, null=True)
    StdUnit = models.CharField(
        max_length=20, blank=True, null=True, default='pza.')
    SalesUnit = models.CharField(
        max_length=20, blank=True, null=True, default='pza.')
    PurchUnit = models.CharField(
        max_length=20, blank=True, null=True, default='pza.')
    Notes = models.TextField(max_length=100, blank=True, null=True)


# Class: Model for Inventory items
# ----------------------------------------------------------------------------
class InventoryModel(TimeStampedModel):

    Item = models.ForeignKey(ItemModel,
                             default=None,
                             related_name='Item',
                             null=True,
                             blank=True)
    Location = models.ForeignKey(
        LocationModel, null=True, blank=True, related_name='Location')
    Qty = models.IntegerField(default=0, null=True)

    def __unicode__(self):
        return "{0}: {1} en {2}".format(self.Item, self.Qty, self.Location)


# Class: Model for history movements
# ----------------------------------------------------------------------------
class MovementHistoryModel(TimeStampedModel):
    RECEPTION = 'REC'
    ADJUSTMENT = 'AJD'
    PICKED = 'PIC'
    SALE = 'SAL'

    TransactionTypes = (
        (RECEPTION, 'Recepción de producto'),
        (ADJUSTMENT, 'Ajuste de stock'),
        (PICKED, 'Selección'),
        (SALE, 'Venta'),
    )

    Item = models.ForeignKey(ItemModel,
                             default=None,
                             related_name='ItemHistory',
                             null=True,
                             blank=True)
    TransactionType = models.CharField(max_length=30, choices=TransactionTypes)
    Date = models.DateTimeField(null=True, blank=True, auto_now=True)
    Location = models.ForeignKey(
        LocationModel, null=True, blank=True, related_name='LocationHistory')
    Notes = models.TextField(max_length=100, blank=True, null=True)
    Qty = models.IntegerField(default=0, null=True)
    Qty_prev = models.IntegerField(default=0, null=True)
    Qty_after = models.IntegerField(default=0, null=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return "{0}: {1} en {2}".format(self.Item, self.Qty, self.Location)


# Class: Model for order movements
# ----------------------------------------------------------------------------
class OrderHistoryModel(TimeStampedModel):
    PURCH = 'PO'
    SALES = 'SO'

    OrderTypes = (
        (PURCH, 'Orden de compra'),
        (SALES, 'Orden de venta'),
    )

    Item = models.ForeignKey(ItemModel,
                             default=None,
                             related_name='OrderHistory',
                             null=True,
                             blank=True)
    Type = models.CharField(max_length=20, choices=OrderTypes)
    DocumentId = models.CharField(max_length=30)
    CustVendName = models.CharField(
        max_length=100, default=None)
    DocumentDate = models.DateField()
    DocumentStatus = models.CharField(max_length=50)
    DocumentTotal = models.DecimalField(
        max_digits=20, decimal_places=2)
    Qty = models.IntegerField(default=0)
    Price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    SubTotal = models.DecimalField(
        max_digits=20, decimal_places=2, default=0.00)

    def __unicode__(self):
        return "{0}: {1} en {2}".format(self.Item, self.Qty, self.DocumentId)

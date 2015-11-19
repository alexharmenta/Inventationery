#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:15:59
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-18 21:22:57
from django.db import models
from Inventationery.core.models import TimeStampedModel


# Function: Get new sequence number for Purchase Order
def Get_PurchId():
    prefix = 'OC-'

    try:
        last = PurchOrderModel.objects.latest('created')
    except:
        last = None

    if last:
        no = int(filter(unicode.isdigit, last.AccountNum))
        no = no + 1
        return prefix + str(no).zfill(5)
    else:
        return prefix + str(1).zfill(5)


# Class: Model for Purchase Order
# ---------------------------------------------------------------------------
class PurchOrderModel(TimeStampedModel):

    # PURCHASE TYPE OPTIONS
    PURCHASE_ORDER = 'PO'
    RESTORED_ORDER = 'RO'

    PURCHASE_TYPE = (
        (PURCHASE_ORDER, 'Orden de compra'),
        (RESTORED_ORDER, 'Orden devuelta'),
    )
    # PURCHASE STATUS OPTIONS
    BACKORDER = 'BAC'
    RECEIVED = 'REC'
    INVOICED = 'INV'
    CANCELED = 'CAN'

    PURCH_STATUS = (
        (BACKORDER, 'Back order'),
        (RECEIVED, 'Recibido'),
        (INVOICED, 'Facturado'),
        (CANCELED, 'Cancelado'),
    )
    # DELIVERY MODE
    HOME = 'HOM'
    BRANCH = 'BRA'

    DLV_MODE = (
        (HOME, 'A domicilio'),
        (BRANCH, 'En sucursal'),
    )

    PurchId = models.CharField(
        max_length=45, default=Get_PurchId, unique=True)
    PurchName = models.CharField(max_length=100)
    PurchaseType = models.CharField(
        max_length=50, choices=PURCHASE_TYPE, default=PURCHASE_ORDER)
    OrderAccount = models.CharField(max_length=100)
    InvoiceAccount = models.CharField(
        max_length=50, default=None, blank=True, null=True)
    PurchStatus = models.CharField(
        max_length=100, default=BACKORDER, choices=PURCH_STATUS)
    # DocumentStatus //Pendiente
    WorkerPurchPlacer = models.CharField(
        max_length=100, blank=True, null=True)  # DirParty-Name
    LanguageCode = models.CharField(
        max_length=5, default='es-mx')  # DirParty-LanguageCode
    DeliveryName = models.CharField(
        max_length=200, blank=True, null=True)  # VendModel-get_PrimaryAddress
    DeliveryDate = models.DateField(blank=True, null=True)
    ConfirmedDlv = models.DateField(blank=True, null=True)
    DlvMode = models.CharField(max_length=20, default=HOME, choices=DLV_MODE)
    CurrencyCode = models.CharField(
        default='MXN', max_length=3)  # VendModel-CurrencyCode
    # Catalogo de pagos a 30 dias
    Payment = models.CharField(max_length=30, blank=True, null=True)
    # Catalogo de tipo de pagos
    PaymMode = models.CharField(max_length=30, blank=True, null=True)
    CashDisc = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)  # Descuento
    CashDiscPercent = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True)  # Descuento en porcentaje

    def __unicode__(self):
        return "{0}".format(self.PurchId)


# Class: Model for Purchase Order
# ---------------------------------------------------------------------------
class PurchLineModel(TimeStampedModel):

    # PURCHASE STATUS OPTIONS
    BACKORDER = 'BAC'
    RECEIVED = 'REC'
    INVOICED = 'INV'
    CANCELED = 'CAN'

    PURCH_STATUS = (
        (BACKORDER, 'Back order'),
        (RECEIVED, 'Recibido'),
        (INVOICED, 'Facturado'),
        (CANCELED, 'Cancelado'),
    )

    ItemId = models.CharField(max_length=20)
    ItemName = models.CharField(max_length=50)
    PurchQty = models.PositiveIntegerField()
    PurchUnit = models.CharField(max_length=10)
    PurchPrice = models.FloatField()
    LineDisc = models.DecimalField(max_digits=10, decimal_places=2)
    LinePercent = models.DecimalField(max_digits=10, decimal_places=2)
    LineAmount = models.DecimalField(max_digits=20, decimal_places=2)
    PurchLineStatus = models.CharField(
        max_length=100, default=BACKORDER, choices=PURCH_STATUS)
    LineNum = models.PositiveSmallIntegerField()
    PurchOrder = models.ForeignKey(
        PurchOrderModel, null=True, blank=True, default=Get_PurchId)

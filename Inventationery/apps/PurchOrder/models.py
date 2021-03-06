#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:15:59
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-26 19:09:43
from django.db import models
from Inventationery.core.models import TimeStampedModel
from Inventationery.apps.Vendor.models import VendorModel
from Inventationery.apps.Inventory.models import ItemModel, LocationModel
from Inventationery.apps.Payments.models import PaymentModel, PaymModeModel
from Inventationery.core.models import Countries


# Function: Get currency codes from Countries model
def Get_CurrencyCodes():
    CurrencyCodes = Countries.objects.values('currency_code')
    Codes_list = ()
    for Currency in CurrencyCodes:
        Codes_list.append()


# Function: Get new sequence number for Purchase Order
def Get_PurchId():
    prefix = 'OC-'

    try:
        last = PurchOrderModel.objects.latest('created')
    except:
        last = None

    if last:
        no = int(filter(unicode.isdigit, last.PurchId))
        no = no + 1
        return str(prefix + str(no).zfill(5))
    else:
        return str(prefix + str(1).zfill(5))


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
    OPEN = 'OPE'
    # BACKORDER = 'BAC'
    RECEIVED = 'REC'
    INVOICED = 'INV'
    PAID = 'PAI'
    CANCELED = 'CAN'
    RECEIVED_PAID = 'RPA'

    PURCH_STATUS = (
        (OPEN, 'Abierta'),
        # (BACKORDER, 'Back order'),
        (RECEIVED, 'Recibido'),
        (INVOICED, 'Facturado'),
        (PAID, 'Pagado'),
        (CANCELED, 'Cancelado'),
        (RECEIVED_PAID, 'Recibido/Pagado'),
    )
    # DOCUMENT STATE OPTIONS
    OPEN = 'Abierto'
    PROCESS = 'Proceso'
    CLOSED = 'Cerrado'

    DOC_STATE = (
        (OPEN, 'Abierto'),
        (PROCESS, 'En proceso'),
        (CLOSED, 'Cerrado'),
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
    PurchStatus = models.CharField(
        max_length=100, default=OPEN, choices=PURCH_STATUS)
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
        default='MXN',
        max_length=3)  # VendModel-CurrencyCode
    # Catalogo de pagos a 30 dias
    Payment = models.ForeignKey(PaymentModel, blank=True, null=True)
    # Catalogo de tipo de pagos
    PaymMode = models.ForeignKey(PaymModeModel, null=True, blank=True)
    Remarks = models.TextField(
        default=None, blank=True, null=True)
    SubTotal = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True)
    Total = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True)
    Paid = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True)
    Balance = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True)

    Enabled = models.BooleanField(default=True)
    DocumentState = models.CharField(
        max_length=20, choices=DOC_STATE, default=CLOSED)

    Vendor = models.ForeignKey(VendorModel, default=None)

    Location = models.ForeignKey(LocationModel, blank=True, null=True)

    def __unicode__(self):
        return "{0}".format(self.PurchId)


# Class: Model for Purchase Order
# ---------------------------------------------------------------------------
class PurchLineModel(TimeStampedModel):

    # PURCHASE STATUS OPTIONS
    BACKORDER = 'BAC'
    RECEIVED = 'REC'
    INVOICED = 'INV'
    PAID = 'PAI'
    CANCELED = 'CAN'

    PURCH_STATUS = (
        (BACKORDER, 'Back order'),
        (RECEIVED, 'Recibido'),
        (INVOICED, 'Facturado'),
        (PAID, 'Pagado'),
        (CANCELED, 'Cancelado'),
    )

    ItemId = models.ForeignKey(ItemModel, blank=True, null=True)
    ItemName = models.CharField(max_length=50, blank=True, null=True)
    PurchQty = models.PositiveIntegerField(blank=True, null=True)
    PurchUnit = models.CharField(max_length=10, blank=True, null=True)
    PurchPrice = models.DecimalField(
        blank=True, null=True, max_digits=10, decimal_places=2)
    LineDisc = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    LinePercent = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    LineAmount = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True)
    PurchLineStatus = models.CharField(max_length=100,
                                       default=BACKORDER,
                                       choices=PURCH_STATUS,
                                       blank=True,
                                       null=True)
    LineNum = models.PositiveSmallIntegerField(blank=True, null=True)
    PurchOrder = models.ForeignKey(
        PurchOrderModel, null=True, blank=True)

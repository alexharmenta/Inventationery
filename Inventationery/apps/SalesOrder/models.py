#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:15:59
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-28 22:28:23
from django.db import models
from Inventationery.core.models import TimeStampedModel
from Inventationery.apps.Customer.models import CustomerModel
from Inventationery.apps.Inventory.models import ItemModel, LocationModel
from Inventationery.apps.Payments.models import PaymentModel, PaymModeModel
from Inventationery.core.models import Countries


# Function: Get currency codes from Countries model
def Get_CurrencyCodes():
    CurrencyCodes = Countries.objects.values('currency_code')
    Codes_list = ()
    for Currency in CurrencyCodes:
        Codes_list.append()


# Function: Get new sequence number for Sales Order
def Get_SalesId():
    prefix = 'OV-'

    try:
        last = SalesOrderModel.objects.latest('created')
    except:
        last = None

    if last:
        no = int(filter(unicode.isdigit, last.SalesId))
        no = no + 1
        return str(prefix + str(no).zfill(5))
    else:
        return str(prefix + str(1).zfill(5))


# Class: Model for Sales Order
# ---------------------------------------------------------------------------
class SalesOrderModel(TimeStampedModel):

    # SALES TYPE OPTIONS
    SALES_ORDER = 'SO'
    RESTORED_ORDER = 'RO'

    SALES_TYPE = (
        (SALES_ORDER, 'Orden de venta'),
        (RESTORED_ORDER, 'Orden devuelta'),
    )
    # SALES STATUS OPTIONS
    OPEN = 'OPE'
    # BACKORDER = 'BAC'
    REDUCED = 'RED'
    INVOICED = 'INV'
    CASHED = 'CAS'
    CANCELED = 'CAN'
    REDUCED_CASHED = 'RCA'

    SALES_STATUS = (
        (OPEN, 'Abierta'),
        # (BACKORDER, 'Back order'),
        (REDUCED, 'Reducido'),
        (INVOICED, 'Facturado'),
        (CASHED, 'Cobrado'),
        (CANCELED, 'Cancelado'),
        (REDUCED_CASHED, 'Reducido/Cobrado'),
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

    SalesId = models.CharField(
        max_length=45, default=Get_SalesId, unique=True)
    SalesName = models.CharField(max_length=100)
    SalesType = models.CharField(
        max_length=50, choices=SALES_TYPE, default=SALES_ORDER)
    SalesStatus = models.CharField(
        max_length=100, default=OPEN, choices=SALES_STATUS)
    # DocumentStatus //Pendiente
    WorkerSalesPlacer = models.CharField(
        max_length=100, blank=True, null=True)  # DirParty-Name
    LanguageCode = models.CharField(
        max_length=5, default='es-mx')  # DirParty-LanguageCode
    DeliveryName = models.CharField(
        max_length=200, blank=True, null=True)  # CustModel-get_PrimaryAddress
    DeliveryDate = models.DateField(blank=True, null=True)
    ConfirmedDlv = models.DateField(blank=True, null=True)
    DlvMode = models.CharField(max_length=20, default=HOME, choices=DLV_MODE)
    CurrencyCode = models.CharField(
        default='MXN',
        max_length=3)  # CustModel-CurrencyCode
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

    Customer = models.ForeignKey(CustomerModel, default=None)

    Location = models.ForeignKey(LocationModel, blank=True, null=True)

    def __unicode__(self):
        return "{0}".format(self.SalesId)


# Class: Model for Sales Order
# ---------------------------------------------------------------------------
class SalesLineModel(TimeStampedModel):

    # SALES STATUS OPTIONS
    BACKORDER = 'BAC'
    REDUCED = 'RED'
    INVOICED = 'INV'
    CASHED = 'CAS'
    CANCELED = 'CAN'

    SALES_STATUS = (
        (BACKORDER, 'Back order'),
        (REDUCED, 'Reducido'),
        (INVOICED, 'Facturado'),
        (CASHED, 'Cobrado'),
        (CANCELED, 'Cancelado'),
    )

    ItemId = models.ForeignKey(ItemModel, blank=True, null=True)
    ItemName = models.CharField(max_length=50, blank=True, null=True)
    SalesQty = models.PositiveIntegerField(blank=True, null=True)
    SalesUnit = models.CharField(max_length=10, blank=True, null=True)
    SalesPrice = models.DecimalField(
        blank=True, null=True, max_digits=10, decimal_places=2)
    LineDisc = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    LinePercent = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    LineAmount = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True)
    SalesLineStatus = models.CharField(max_length=100,
                                       default=BACKORDER,
                                       choices=SALES_STATUS,
                                       blank=True,
                                       null=True)
    LineNum = models.PositiveSmallIntegerField(blank=True, null=True)
    SalesOrder = models.ForeignKey(
        SalesOrderModel, null=True, blank=True)

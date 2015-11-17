#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:14:39
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-16 19:34:44
from django.db import models
from Inventationery.apps.DirParty.models import DirPartyModel
# Create your models here.


class LogisticsPostalAddressModel(models.Model):

    BUSINESS = 'BUS'
    DELIVERY = 'DEL'
    HOME = 'HOM'
    INVOICE = 'INV'
    PAYMENT = 'PAY'
    SERVICE = 'SER'
    OTHER = 'OTH'

    PURPOSE_CHOICES = (
        ('BUSINESS', 'Negocio'),
        ('DELIVERY', 'Entrega'),
        ('HOME', 'Particular'),
        ('INVOICE', 'Factura'),
        ('PAYMENT', 'Pago'),
        ('SERVICE', 'Servicio'),
        ('OTHER', 'Otro'),
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    Description = models.CharField(max_length=30, blank=True, null=True)
    Purpose = models.CharField(
        max_length=30, choices=PURPOSE_CHOICES, default=BUSINESS)
    CountryRegionId = models.CharField(max_length=3, default='MEX')
    ZipCode = models.CharField(max_length=5, blank=True, null=True)
    Street = models.CharField(max_length=30, blank=True, null=True)
    StreetNumber = models.PositiveSmallIntegerField(blank=True, null=True)
    BuildingCompliment = models.CharField(max_length=10, blank=True, null=True)
    City = models.CharField(max_length=30, blank=True, null=True)
    State = models.CharField(max_length=30, blank=True, null=True)
    IsPrimary = models.BooleanField(default=False)

    Party = models.ForeignKey(DirPartyModel)

    def address_info(self):
        Street = str(self.Street)
        StreetNumber = str(self.StreetNumber)
        BuildingCompliment = str(self.BuildingCompliment)
        City = str(self.City)
        State = str(self.State)
        Country = str(self.CountryRegionId)

        address = Street + " " + StreetNumber + " " + BuildingCompliment + \
            ", " + City + " " + State + ", " + Country + "."

        return address

    def __unicode__(self):
        return self.address_info()

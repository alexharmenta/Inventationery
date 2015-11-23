#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:13:48
# @Last Modified by:   harmenta
# @Last Modified time: 2015-11-23 10:53:52
from django.db import models
from Inventationery.apps.DirParty.models import DirPartyModel
from Inventationery.core.models import TimeStampedModel


# Class: Model for Logistics Electronic Address
# ----------------------------------------------------------------------------
class LogisticsElectronicAddressModel(TimeStampedModel):

    TELEPHONE = 'TEL'
    CELLPHONE = 'CEL'
    EMAIL = 'EMA'
    URL = 'URL'
    FAX = 'FAX'

    TYPE = (
        (TELEPHONE, 'Teléfono'),
        (CELLPHONE, 'Celular'),
        (EMAIL, 'Email'),
        (URL, 'Página web'),
        (FAX, 'Fax'),
    )

    Description = models.CharField(max_length=30, blank=True, null=True)
    Type = models.CharField(max_length=30, choices=TYPE, default=TELEPHONE)
    Contact = models.CharField(max_length=200, blank=True, null=True)

    IsPrimary = models.BooleanField(default=False)

    Party = models.ForeignKey(DirPartyModel)

    def __unicode__(self):
        return self.Description

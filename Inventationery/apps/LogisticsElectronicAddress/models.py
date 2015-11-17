#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:13:48
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-16 19:35:00
from django.db import models
from Inventationery.apps.DirParty.models import DirPartyModel
# Create your models here.


class LogisticsElectronicAddressModel(models.Model):

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

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    Description = models.CharField(max_length=30, blank=True, null=True)
    Type = models.CharField(max_length=30, choices=TYPE, default=TELEPHONE)
    Contact = models.CharField(max_length=200, blank=True, null=True)

    IsPrimary = models.BooleanField(default=False)

    Party = models.ForeignKey(DirPartyModel)

    def __unicode__(self):
        return self.Description

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmenta
# @Date:   2015-12-24 11:10:51
# @Last Modified by:   harmenta
# @Last Modified time: 2015-12-28 17:10:47
from django.db import models
from Inventationery.core.models import TimeStampedModel
from Inventationery.apps.DirParty.models import DirPartyModel


class CompanyInfoModel(TimeStampedModel):
    LegalEntity = 'LEGE'
    LegalPerson = 'LEGP'
    ForeignCompany = 'FORE'

    CompanyTypeChoices = {
        (LegalEntity, 'Entidad jurídica'),
        (LegalPerson, 'Persona jurídica'),
        (ForeignCompany, 'Companía extranjera'),
    }
    # Table fields
    Description = models.TextField(blank=True, null=True)
    CompanyType = models.CharField(max_length=20, choices=CompanyTypeChoices)
    CoRegNum = models.CharField(max_length=13, blank=True)
    VATNum = models.CharField(max_length=13, blank=True)
    DataArea = models.CharField(max_length=4)
    CompanyImage = models.ImageField(
        upload_to='CompanyInfo', null=True, blank=True, default=None)
    # Relations
    Party = models.OneToOneField(DirPartyModel,
                                 default=None,
                                 related_name='CompanyParty',
                                 null=True,
                                 blank=True)
    # Contact Info
    Phone = models.CharField(max_length=50, blank=True, null=True)
    Fax = models.CharField(max_length=50, blank=True, null=True)
    URL = models.URLField(max_length=100, blank=True, null=True)
    Email = models.EmailField(max_length=100, blank=True, null=True)

    # Address Info
    AddressDescription = models.CharField(max_length=30, blank=True, null=True)
    Purpose = models.CharField(max_length=30, default='NEGOCIO')
    CountryRegionId = models.CharField(max_length=3, default='MEX')
    ZipCode = models.CharField(max_length=5, blank=True, null=True)
    Street = models.CharField(max_length=30, blank=True, null=True)
    StreetNumber = models.PositiveSmallIntegerField(blank=True, null=True)
    BuildingCompliment = models.CharField(max_length=10, blank=True, null=True)
    City = models.CharField(max_length=30, blank=True, null=True)
    State = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        return self.Party.NameAlias

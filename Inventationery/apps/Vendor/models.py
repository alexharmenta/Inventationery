#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex Armenta
# @Date:   2015-11-17 12:15:05
# @Last Modified by:   harmenta
# @Last Modified time: 2015-11-19 17:14:05
from django.db import models
from Inventationery.core.models import TimeStampedModel
from Inventationery.apps.DirParty.models import DirPartyModel
from Inventationery.apps.LogisticsPostalAddress.models import (
    LogisticsPostalAddressModel)
from Inventationery.apps.LogisticsElectronicAddress.models import (
    LogisticsElectronicAddressModel)


# Function: Get new sequence number for vendor AccountNum
def Get_Account_Num():
    prefix = 'P-'

    try:
        last = VendorModel.objects.latest('created')
    except:
        last = None

    if last:
        no = int(filter(unicode.isdigit, last.AccountNum))
        no = no + 1
        return prefix + str(no).zfill(5)
    else:
        return prefix + str(1).zfill(5)


# Class: Model for Vendor
# ----------------------------------------------------------------------------
class VendorModel(TimeStampedModel):

    # Person options
    PERSON_TYPE = 'PER'
    PARTY_TYPE = 'PAR'

    ACCOUNT_TYPE = (
        (PERSON_TYPE, 'Persona'),
        (PARTY_TYPE, 'Organización'),
    )
    # Group options
    LOCAL_GROUP = 'Loc'
    INTERNATIONAL_GROUP = 'Int'
    NATIONAL_GROUP = 'Nat'

    VEND_GROUP = (
        (LOCAL_GROUP, 'Local'),
        (NATIONAL_GROUP, 'Nacional'),
        (INTERNATIONAL_GROUP, 'Internacional'),
    )

    AccountNum = models.CharField(default=Get_Account_Num,
                                  unique=True,
                                  max_length=45)
    AccountType = models.CharField(max_length=3,
                                   choices=ACCOUNT_TYPE,
                                   default=PARTY_TYPE)
    OneTimeVendor = models.BooleanField(default=False)
    VendGroup = models.CharField(max_length=3,
                                 choices=VEND_GROUP,
                                 default=LOCAL_GROUP)
    CreditLimit = models.DecimalField(max_digits=15,
                                      decimal_places=2,
                                      blank=True,
                                      null=True)
    CurrencyCode = models.CharField(default='MXN', max_length=3)
    VATNum = models.CharField(max_length=13, blank=True)
    Notes = models.TextField(max_length=200, blank=True)

    # Relations
    Party = models.OneToOneField(DirPartyModel,
                                 default=None,
                                 null=True,
                                 blank=True,
                                 related_name='VendorParty',)

    def __unicode__(self):
        return "{0}".format(self.AccountNum)

    def get_PrimaryAddress(self):
        try:
            Address = LogisticsPostalAddressModel.objects.filter(
                Party=self.Party, IsPrimary=True)[:1].get()
            return Address.address_info()
        except:
            return ''

    def get_PrimaryElectronic(self):
        try:
            Electronic = LogisticsElectronicAddressModel.objects.filter(
                Party=self.Party, IsPrimary=True)[:1].get()
            return Electronic.Contact
        except:
            return ''

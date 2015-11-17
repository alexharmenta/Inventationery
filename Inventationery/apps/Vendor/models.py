#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:22:12
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-16 20:04:55
from django.db import models
from Inventationery.apps.DirParty.models import DirPartyModel
from Inventationery.apps.LogisticsPostalAddress.models import (
    LogisticsPostalAddressModel)
from Inventationery.apps.LogisticsElectronicAddress.models import (
    LogisticsElectronicAddressModel)
# Create your models here.


def Get_Account_Num():
    prefix = 'P'

    try:
        last = VendModel.objects.latest('created')
    except:
        last = None

    if last:
        no = int(last.AccountNum[1:])
        no = str(no + 1)
        return prefix + no
    else:
        return prefix + str(0001)


class VendModel(models.Model):

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

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    AccountNum = models.CharField(default=Get_Account_Num,
                                  unique=True,
                                  max_length=5)
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
    VATNum = models.CharField(max_length=13, blank=True, null=True)
    Notes = models.TextField(max_length=200, blank=True, null=True)

    # Relations
    Party = models.OneToOneField(DirPartyModel,
                                 default=None,
                                 null=True,
                                 blank=True,)

    def __unicode__(self):
        return "{0}".format(self.AccountNum)

    def get_PrimaryAddress(self):
        Address = LogisticsPostalAddressModel.objects.filter(
            Party=self.Party, IsPrimary=True)[:1].get()
        return Address.address_info()

    def get_PrimaryElectronic(self):
        Electronic = LogisticsElectronicAddressModel.objects.filter(
            Party=self.Party, IsPrimary=True)[:1].get()
        return Electronic.Contact

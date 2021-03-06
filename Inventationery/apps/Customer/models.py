#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex Armenta
# @Date:   2015-11-17 12:15:05
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-28 19:52:48
from django.db import models
from Inventationery.core.models import TimeStampedModel
from Inventationery.apps.DirParty.models import DirPartyModel
from Inventationery.apps.LogisticsPostalAddress.models import (
    LogisticsPostalAddressModel)
from Inventationery.apps.LogisticsElectronicAddress.models import (
    LogisticsElectronicAddressModel)


# Function: Get new sequence number for customer AccountNum
def Get_Account_Num():
    prefix = 'C-'

    try:
        last = CustomerModel.objects.latest('created')
    except:
        last = None

    if last:
        no = int(filter(unicode.isdigit, last.AccountNum))
        no = no + 1
        return prefix + str(no).zfill(5)
    else:
        return prefix + str(1).zfill(5)


# Class: Model for Customer
# ----------------------------------------------------------------------------
class CustomerModel(TimeStampedModel):

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

    CUST_GROUP = (
        (LOCAL_GROUP, 'Local'),
        (NATIONAL_GROUP, 'Nacional'),
        (INTERNATIONAL_GROUP, 'Internacional'),
    )

    AccountNum = models.CharField(default=Get_Account_Num,
                                  unique=True,
                                  max_length=45)
    AccountType = models.CharField(max_length=3,
                                   choices=ACCOUNT_TYPE,
                                   default=PERSON_TYPE)
    OneTimeCustomer = models.BooleanField(default=False)
    CustGroup = models.CharField(max_length=3,
                                 choices=CUST_GROUP,
                                 default=LOCAL_GROUP)
    CreditLimit = models.DecimalField(max_digits=15,
                                      decimal_places=2,
                                      blank=True,
                                      null=True)
    Discount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    CurrencyCode = models.CharField(default='MXN', max_length=3)
    VATNum = models.CharField(max_length=13, blank=True)
    Notes = models.TextField(max_length=200, blank=True)

    # Relations
    Party = models.OneToOneField(DirPartyModel,
                                 default=None,
                                 related_name='CustomerParty',
                                 null=True,
                                 blank=True)

    def __unicode__(self):
        return self.AccountNum

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

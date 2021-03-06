#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:22:39
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-28 19:32:30
from django import forms
from .models import CustomerModel
from Inventationery.apps.DirParty.models import DirPartyModel
from Inventationery.apps.LogisticsPostalAddress.models import (
    LogisticsPostalAddressModel)
from Inventationery.apps.LogisticsElectronicAddress.models import (
    LogisticsElectronicAddressModel)


# Class: Form for CustomerModel
# ----------------------------------------------------------------------------
class CustomerForm(forms.ModelForm):

    class Meta:
        model = CustomerModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['AccountNum'].widget.attrs['readonly'] = True
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['AccountType'].widget.attrs['readonly'] = True

    def clean_sku(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.AccountNum
        else:
            return self.cleaned_data['AccountNum']


# Class: Form for DirPartyModel
# ----------------------------------------------------------------------------
class PartyForm(forms.ModelForm):

    class Meta:
        model = DirPartyModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PartyForm, self).__init__(*args, **kwargs)


# Class: Form for LogisticsPostalAddressModel
# ----------------------------------------------------------------------------
class LogisticsPostalForm(forms.ModelForm):

    class Meta:
        model = LogisticsPostalAddressModel
        fields = '__all__'


# Class: Form for LogisticsElectronicAddressModel
# ----------------------------------------------------------------------------
class LogisticsElectronicForm(forms.ModelForm):

    class Meta:
        model = LogisticsElectronicAddressModel
        fields = '__all__'

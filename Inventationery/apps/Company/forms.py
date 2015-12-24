#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmenta
# @Date:   2015-12-24 12:13:37
# @Last Modified by:   harmenta
# @Last Modified time: 2015-12-24 12:16:49
from django import forms
from .models import CompanyInfoModel
from Inventationery.apps.DirParty.models import DirPartyModel
from Inventationery.apps.LogisticsPostalAddress.models import (
    LogisticsPostalAddressModel)
from Inventationery.apps.LogisticsElectronicAddress.models import (
    LogisticsElectronicAddressModel)


class CompanyInfoForm(forms.ModelForm):

    class Meta:
        model = CompanyInfoModel
        fields = '__all__'


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

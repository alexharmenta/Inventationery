#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:22:39
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-17 20:23:38
from django import forms
from .models import VendorModel
from Inventationery.apps.DirParty.models import DirPartyModel
from Inventationery.apps.LogisticsPostalAddress.models import (
    LogisticsPostalAddressModel)
from Inventationery.apps.LogisticsElectronicAddress.models import (
    LogisticsElectronicAddressModel)


class VendorForm(forms.ModelForm):

    class Meta:
        model = VendorModel
        fields = ('AccountNum',
                  'AccountType',
                  'OneTimeVendor',
                  'VendGroup',
                  'CreditLimit',
                  'CurrencyCode',
                  'VATNum',
                  'Notes',
                  'Party')

    def __init__(self, *args, **kwargs):
        super(VendorForm, self).__init__(*args, **kwargs)
        self.fields['AccountNum'].widget.attrs['readonly'] = True


class PartyForm(forms.ModelForm):

    class Meta:
        model = DirPartyModel
        fields = ('Name',
                  'NameAlias',
                  'LanguageCode',
                  'SecondName',
                  'FirstLastName',
                  'SecondLastName',
                  'Gender')

    def __init__(self, *args, **kwargs):
        super(PartyForm, self).__init__(*args, **kwargs)


class LogisticsPostalForm(forms.ModelForm):

    class Meta:
        model = LogisticsPostalAddressModel
        fields = ('Description',
                  'Purpose',
                  'CountryRegionId',
                  'ZipCode',
                  'Street',
                  'StreetNumber',
                  'BuildingCompliment',
                  'City',
                  'State',
                  'IsPrimary',)

"""
class BasePostalFormSet(BaseFormSet):

    def clean(self):
        if any(self.errors):
            return

        primarys = []
        descriptions = []
        duplicates = False

        for form in self.forms:
            if form.cleaned_data:
                IsPrimary = form.cleaned_data['IsPrimary']
                Description = form.cleaned_data['Description']

                if IsPrimary and Description:
                    if IsPrimary in primarys:
                        duplicates = True
                    primarys.append(IsPrimary)

                    if Description in descriptions:
                        duplicates = True
                    descriptions.append(Description)

                if duplicates:
                    raise forms.ValidationError(
                        'Solo una dirección puede ser principal y no debe repetirse la descripción',
                        code='duplicate_postal',
                    )

                if not IsPrimary:
                    raise forms.ValidationError(
                        'Selecciona una dirección como principal',
                        code='missing_postal_primary',
                    )
"""


class LogisticsElectronicForm(forms.ModelForm):

    class Meta:
        model = LogisticsElectronicAddressModel
        fields = ('Description',
                  'Type',
                  'Contact',
                  'IsPrimary',)

"""
class BaseElectronicFormSet(BaseFormSet):

    def clean(self):
        if any(self.errors):
            return

        primarys = []
        descriptions = []
        duplicates = False

        for form in self.forms:
            if form.cleaned_data:
                IsPrimary = form.cleaned_data['IsPrimary']
                Description = form.cleaned_data['Description']

                if IsPrimary and Description:
                    if IsPrimary in primarys:
                        duplicates = True
                    primarys.append(IsPrimary)

                    if Description in descriptions:
                        duplicates = True
                    descriptions.append(Description)

                if duplicates:
                    raise forms.ValidationError(
                        'Solo un contacto puede ser principal y no debe repetirse la descripción',
                        code='duplicate_electronic',
                    )

                if not IsPrimary:
                    raise forms.ValidationError(
                        'Selecciona un contacto como principal',
                        code='missing_electronic_primary',
                    )
"""

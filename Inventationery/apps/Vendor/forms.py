#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:22:39
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-16 19:36:15
from django import forms
from django.forms.formsets import BaseFormSet
from .models import VendModel
from Inventationery.apps.DirParty.models import DirPartyModel
from Inventationery.apps.LogisticsPostalAddress.models import (
    LogisticsPostalAddressModel)
from Inventationery.apps.LogisticsElectronicAddress.models import (
    LogisticsElectronicAddressModel)


class VendorForm(forms.ModelForm):

    class Meta:
        model = VendModel
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


class BasePostalFormSet(BaseFormSet):

    def clean(self):
        """Checks that no two articles have the same title."""
        if any(self.errors):
            # Don't bother validating the formset unless each form is valid on
            # its own
            return
        descriptions = []
        primarys = []
        for form in self.forms:
            description = form.cleaned_data['Description']
            primary = form.cleaned_data['IsPrimary']
            if description in descriptions:
                raise forms.ValidationError(
                    "No repita el nombre de las direcciones")
            if primary in primarys:
                raise forms.ValidationError(
                    "Solo debe haber una dirección principal"
                )
            descriptions.append(description)


class LogisticsElectronicForm(forms.ModelForm):

    class Meta:
        model = LogisticsElectronicAddressModel
        fields = ('Description',
                  'Type',
                  'Contact',
                  'IsPrimary',)


class BaseElectronicFormSet(BaseFormSet):

    def clean(self):
        """Adds validation to know if an address
        is already a primary address"""
        if any(self.errors):
            return

        IsPrimarys = []
        duplicates = False

        for form in self.forms:
            if form.cleaned_data:
                IsPrimary = form.cleaned_data['IsPrimary']

                if IsPrimary:
                    if IsPrimary in IsPrimarys:
                        duplicates = True
                    IsPrimarys.append(IsPrimary)

                if duplicates:
                    raise forms.ValidationError(
                        'Solo un contacto puede ser principal.',
                        code='duplicate_primary',
                    )

                if not IsPrimary:
                    raise forms.ValidationError(
                        'Selecciona un contacto como principal',
                        code='missing_primary',
                    )

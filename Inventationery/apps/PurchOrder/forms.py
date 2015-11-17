#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:16:42
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-16 20:03:06
from django import forms
from django.forms.formsets import BaseFormSet
from .models import PurchOrderModel, PurchLineModel
from Inventationery.apps.Vendor.models import VendModel
from Inventationery.apps.Inventory.models import InventModel


class PurchOrderForm(forms.ModelForm):
    OrderAccount = forms.ModelChoiceField(queryset=VendModel.objects.all())
    queryset = VendModel.objects.all()
    print queryset
    InvoiceAccount = forms.ModelChoiceField(queryset=VendModel.objects.all())

    def __init__(self, *args, **kwargs):
        super(PurchOrderForm, self).__init__(*args, **kwargs)
        # Making name require
        # self.fields['OrderAccount'].required = True

    class Meta:
        model = PurchOrderModel
        exclude = ('modified',)


class PurchOrderLinesForm(forms.ModelForm):
    ItemId = forms.ModelChoiceField(queryset=InventModel.objects.all())

    class Meta:
        model = PurchLineModel
        exclude = ('modified',)


class BasePurchLineFormSet(BaseFormSet):

    def clean(self):
        """Adds validation to know if an address
        is already a primary address"""
        if any(self.errors):
            return

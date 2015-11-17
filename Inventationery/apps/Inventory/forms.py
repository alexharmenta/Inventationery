#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:12:08
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-16 19:12:14
from django import forms
from .models import InventModel


class InventForm(forms.ModelForm):

    class Meta:
        model = InventModel
        fields = ('ItemId',
                  'ItemName',
                  'Description',
                  'UnitId',
                  'PrimaryVendor',
                  'Price',
                  'VendorPrice',
                  'ItemImage',)

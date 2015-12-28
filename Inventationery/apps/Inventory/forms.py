#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:12:08
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-27 13:23:03
from django import forms
from .models import (ItemModel, ItemVendorModel,
                     InventoryModel, LocationModel,
                     MovementHistoryModel, EcoResProductModel,
                     OrderHistoryModel)


# Class: Form for ItemModel
# ----------------------------------------------------------------------------
class ItemForm(forms.ModelForm):

    class Meta:
        model = ItemModel
        fields = '__all__'


# Class: Form for ItemVendorModel
# ----------------------------------------------------------------------------
class ItemVendorForm(forms.ModelForm):

    class Meta:
        model = ItemVendorModel
        fields = '__all__'


# Class: Form for LocationModel
# ----------------------------------------------------------------------------
class LocationForm(forms.ModelForm):

    class Meta:
        model = LocationModel
        fields = '__all__'


# Class: Form for LocationModel
# ----------------------------------------------------------------------------
class EcoResProductForm(forms.ModelForm):

    class Meta:
        model = EcoResProductModel
        fields = '__all__'


# Class: Form for InventoryModel
# ----------------------------------------------------------------------------
class InventoryForm(forms.ModelForm):

    class Meta:
        model = InventoryModel
        fields = '__all__'


# Class: Form for MovementHistoryModel
# ----------------------------------------------------------------------------
class MovementHistoryForm(forms.ModelForm):

    class Meta:
        model = MovementHistoryModel
        fields = '__all__'


# Class: Form for OrderHistoryModel
# ----------------------------------------------------------------------------
class OrderHistoryForm(forms.ModelForm):

    class Meta:
        model = OrderHistoryModel
        fields = '__all__'

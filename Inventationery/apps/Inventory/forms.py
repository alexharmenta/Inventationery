#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:12:08
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-10 20:28:34
from django import forms
from .models import ItemModel, InventoryModel, LocationModel


# Class: Form for ItemModel
# ----------------------------------------------------------------------------
class ItemForm(forms.ModelForm):

    class Meta:
        model = ItemModel
        fields = '__all__'


# Class: Form for ItemModel
# ----------------------------------------------------------------------------
class InventoryForm(forms.ModelForm):

    class Meta:
        model = InventoryModel
        fields = '__all__'


# Class: Form for LocationModel
# ----------------------------------------------------------------------------
class LocationForm(forms.ModelForm):

    class Meta:
        model = LocationModel
        fields = '__all__'

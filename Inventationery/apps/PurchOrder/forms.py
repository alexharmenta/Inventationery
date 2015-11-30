#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:16:42
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-29 17:50:39
from django import forms
from .models import PurchOrderModel, PurchLineModel


class PurchOrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PurchOrderForm, self).__init__(*args, **kwargs)
        self.fields['PurchStatus'].widget.attrs['readonly'] = True

    class Meta:
        model = PurchOrderModel
        fields = '__all__'


class PurchOrderLinesForm(forms.ModelForm):

    class Meta:
        model = PurchLineModel
        fields = '__all__'

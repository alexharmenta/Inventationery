#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:16:42
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-28 20:53:30
from django import forms
from .models import SalesOrderModel, SalesLineModel


class SalesOrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SalesOrderForm, self).__init__(*args, **kwargs)
        self.fields['SalesStatus'].widget.attrs['readonly'] = True

    class Meta:
        model = SalesOrderModel
        fields = '__all__'


class SalesOrderLinesForm(forms.ModelForm):

    class Meta:
        model = SalesLineModel
        fields = '__all__'

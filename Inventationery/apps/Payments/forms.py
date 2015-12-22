#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-12-20 22:18:47
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-20 22:20:29
from django import forms
from .models import PaymentModel, PaymModeModel


# Class: Form for Payment
# ----------------------------------------------------------------------------
class PaymentForm(forms.ModelForm):

    class Meta:
        model = PaymentModel
        fields = '__all__'


# Class: Form for Payment Mode
# ----------------------------------------------------------------------------
class PaymModeForm(forms.ModelForm):

    class Meta:
        model = PaymModeModel
        fields = '__all__'

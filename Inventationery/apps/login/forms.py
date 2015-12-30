#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-12-29 23:06:32
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-29 23:07:45
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={
                                   'type': 'password'
                               }))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:22:12
# @Last Modified by:   harmenta
# @Last Modified time: 2015-11-17 13:10:14
from django.contrib import admin
from .models import VendorModel

# Register your models here.
admin.site.register(VendorModel)

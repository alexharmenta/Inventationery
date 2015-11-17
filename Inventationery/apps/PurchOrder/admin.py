#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:15:59
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-16 19:16:33
from django.contrib import admin
from .models import PurchOrderModel, PurchLineModel

# Register your models here.
admin.site.register(PurchOrderModel)
admin.site.register(PurchLineModel)

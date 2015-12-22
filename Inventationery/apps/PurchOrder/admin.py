#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:15:59
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-20 21:28:21
from django.contrib import admin
from .models import (PurchOrderModel, PurchLineModel,
                     PaymentModel, PaymModeModel)

# Register your models here.
admin.site.register(PurchOrderModel)
admin.site.register(PurchLineModel)
admin.site.register(PaymentModel)
admin.site.register(PaymModeModel)

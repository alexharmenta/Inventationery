#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:10:36
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-27 13:19:09
from django.contrib import admin
from .models import (ItemModel, InventoryModel, LocationModel,
                     ItemVendorModel, MovementHistoryModel,
                     EcoResProductModel, OrderHistoryModel)
# Register your models here.
admin.site.register(ItemModel)
admin.site.register(InventoryModel)
admin.site.register(LocationModel)
admin.site.register(ItemVendorModel)
admin.site.register(MovementHistoryModel)
admin.site.register(EcoResProductModel)
admin.site.register(OrderHistoryModel)

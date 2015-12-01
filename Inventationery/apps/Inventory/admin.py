#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:10:36
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-30 19:39:17
from django.contrib import admin
from .models import ItemModel, InventoryModel
# Register your models here.
admin.site.register(ItemModel)
admin.site.register(InventoryModel)

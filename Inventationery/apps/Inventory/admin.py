#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:10:36
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-16 19:11:00
from django.contrib import admin
from .models import InventModel
# Register your models here.
admin.site.register(InventModel)

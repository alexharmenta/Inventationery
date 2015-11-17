#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:22:12
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-16 19:22:28
from django.contrib import admin
from .models import VendModel

# Register your models here.
admin.site.register(VendModel)

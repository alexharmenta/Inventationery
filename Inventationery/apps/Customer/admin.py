#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:22:12
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-28 19:32:16
from django.contrib import admin
from .models import CustomerModel

# Register your models here.
admin.site.register(CustomerModel)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:15:59
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-28 21:36:26
from django.contrib import admin
from .models import (SalesOrderModel, SalesLineModel)

# Register your models here.
admin.site.register(SalesOrderModel)
admin.site.register(SalesLineModel)

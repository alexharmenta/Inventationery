#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:23:26
# @Last Modified by:   harmenta
# @Last Modified time: 2015-11-18 16:49:49
from django.conf.urls import url
from .views import createVendorView
from .views import VendorList, DeleteVendorView, UpdateVendorView

urlpatterns = [
    url(r'^vendor/new/$', createVendorView, name='new'),
    url(r'^vendor/$', VendorList.as_view(), name='list'),
    url(r'^vendor/delete/(?P<pk>[-\w]+)/$',
        DeleteVendorView.as_view(), name='delete'),
    url(r'^vendor/update/(?P<AccountNum>[-\w]+)/$',
        UpdateVendorView.as_view(), name='update'),
]

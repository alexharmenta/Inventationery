#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:23:26
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-18 19:37:05
from django.conf.urls import url
from .views import createVendorView
from .views import VendorList, DeleteVendorView, updateVendorView

urlpatterns = [
    url(r'^vendor/new/$', createVendorView, name='new'),
    url(r'^vendor/$', VendorList.as_view(), name='list'),
    url(r'^vendor/delete/(?P<pk>[-\w]+)/$',
        DeleteVendorView.as_view(), name='delete'),
    url(r'^vendor/update/(?P<AccountNum>[-\w]+)/$',
        updateVendorView, name='update'),
]

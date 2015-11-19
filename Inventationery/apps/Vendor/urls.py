#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:23:26
# @Last Modified by:   harmenta
# @Last Modified time: 2015-11-19 17:25:11
from django.conf.urls import url
from .views import createVendorView
from .views import VendorListView, DeleteVendorView, updateVendorView

urlpatterns = [
    url(r'^vendor/new/$', createVendorView, name='new'),
    url(r'^vendor/$', VendorListView.as_view(), name='list'),
    url(r'^vendor/delete/(?P<pk>[-\w]+)/$',
        DeleteVendorView.as_view(), name='delete'),
    url(r'^vendor/update/(?P<AccountNum>[-\w]+)/$',
        updateVendorView, name='update'),
]

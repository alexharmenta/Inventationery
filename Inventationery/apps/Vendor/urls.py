#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:23:26
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-21 20:52:01
from django.conf.urls import url
from .views import createVendorView
from .views import (VendorListView, DeleteVendorView,
                    updateVendorView, export_csv, export_pdf)

urlpatterns = [
    url(r'^vendor/new/$', createVendorView, name='new'),
    url(r'^vendor/$', VendorListView.as_view(), name='list'),
    url(r'^vendor/delete/(?P<pk>[-\w]+)/$',
        DeleteVendorView.as_view(), name='delete'),
    url(r'^vendor/update/(?P<AccountNum>[-\w]+)/$',
        updateVendorView, name='update'),
    url(r'^vendor/export/cvs/$', export_csv, name='csv'),
    url(r'^vendor/export/pdf/$', export_pdf, name='pdf'),
]

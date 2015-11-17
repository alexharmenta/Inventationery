#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:21:37
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-16 19:21:39
from django.conf.urls import url
from .views import PurchOrderListView, PurchOrderCreateView

urlpatterns = [
    url(r'^purch_orders/new/$', PurchOrderCreateView.as_view(), name='new'),
    url(r'^purch_orders/$', PurchOrderListView.as_view(), name='list'),
    # url(r'^vendors/delete/(?P<pk>[-\w]+)/$',
    #    DeleteVendorView.as_view(), name='delete'),
    # url(r'^vendors/update/(?P<pk>[-\w]+)/$',
    #    UpdateVendorView.as_view(), name='update'),
]

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:21:37
# @Last Modified by:   harmenta
# @Last Modified time: 2015-11-19 17:34:04
from django.conf.urls import url
from .views import (PurchOrderListView,
                    createPurchOrderView, updatePurchOrderView)

urlpatterns = [
    url(r'^purch_orders/new/$', createPurchOrderView, name='new'),
    url(r'^purch_orders/$', PurchOrderListView.as_view(), name='list'),
    url(r'^purch_orders/update/(?P<PurchId>[-\w]+)/$',
        updatePurchOrderView, name='update'),
    # url(r'^vendors/update/(?P<pk>[-\w]+)/$',
    #    UpdateVendorView.as_view(), name='update'),
]

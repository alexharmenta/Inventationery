#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:21:37
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-19 19:43:46
from django.conf.urls import url
from .views import (PurchOrderListView,
                    createPurchOrderView,
                    updatePurchOrderView,
                    DeletePurchOrderView)

urlpatterns = [
    url(r'^purch_orders/new/$', createPurchOrderView, name='new'),
    url(r'^purch_orders/$', PurchOrderListView.as_view(), name='list'),
    url(r'^purch_orders/update/(?P<PurchId>[-\w]+)/$',
        updatePurchOrderView, name='update'),
    url(r'^vendors/delete/(?P<pk>[-\w]+)/$',
        DeletePurchOrderView.as_view(), name='delete'),
]

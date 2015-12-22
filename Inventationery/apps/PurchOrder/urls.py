#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:21:37
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-21 22:10:00
from django.conf.urls import url
from .views import (PurchOrderListView,
                    PurchOrderRecentListView,
                    PurchOrderOpenListView,
                    PurchOrderReceivedListView,
                    PurchOrderPaidListView,
                    createPurchOrderView,
                    updatePurchOrderView,
                    DeletePurchOrderView,
                    export_csv, export_pdf)

urlpatterns = [
    url(r'^purch_orders/$', PurchOrderListView.as_view(), name='list'),
    url(r'^purch_orders/recent/$',
        PurchOrderRecentListView.as_view(), name='recent'),
    url(r'^purch_orders/open/$',
        PurchOrderOpenListView.as_view(), name='open'),
    url(r'^purch_orders/received/$',
        PurchOrderReceivedListView.as_view(), name='received'),
    url(r'^purch_orders/paid/$',
        PurchOrderPaidListView.as_view(), name='paid'),
    url(r'^purch_orders/new/$', createPurchOrderView, name='new'),
    url(r'^purch_orders/update/(?P<PurchId>[-\w]+)/$',
        updatePurchOrderView, name='update'),
    url(r'^purch_orders/delete/(?P<pk>[-\w]+)/$',
        DeletePurchOrderView.as_view(), name='delete'),

    url(r'^purch_orders/export/cvs/$', export_csv, name='csv'),
    url(r'^purch_orders/export/pdf/$', export_pdf, name='pdf'),
]

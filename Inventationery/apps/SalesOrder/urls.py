#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:21:37
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-28 21:48:05
from django.conf.urls import url
from .views import (SalesOrderListView,
                    SalesOrderRecentListView,
                    SalesOrderOpenListView,
                    SalesOrderSentListView,
                    SalesOrderChargedListView,
                    createSalesOrderView,
                    updateSalesOrderView,
                    DeleteSalesOrderView,
                    export_csv, export_pdf)

urlpatterns = [
    url(r'^sales_orders/$', SalesOrderListView.as_view(), name='list'),
    url(r'^sales_orders/recent/$',
        SalesOrderRecentListView.as_view(), name='recent'),
    url(r'^sales_orders/open/$',
        SalesOrderOpenListView.as_view(), name='open'),
    url(r'^sales_orders/sent/$',
        SalesOrderSentListView.as_view(), name='sent'),
    url(r'^sales_orders/charged/$',
        SalesOrderChargedListView.as_view(), name='charged'),
    url(r'^sales_orders/new/$', createSalesOrderView, name='new'),
    url(r'^sales_orders/update/(?P<SalesId>[-\w]+)/$',
        updateSalesOrderView, name='update'),
    url(r'^sales_orders/delete/(?P<pk>[-\w]+)/$',
        DeleteSalesOrderView.as_view(), name='delete'),

    url(r'^sales_orders/export/cvs/$', export_csv, name='csv'),
    url(r'^sales_orders/export/pdf/$', export_pdf, name='pdf'),
]

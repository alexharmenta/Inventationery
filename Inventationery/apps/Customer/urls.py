#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:23:26
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-28 19:33:51
from django.conf.urls import url
from .views import createCustomerView
from .views import (CustomerListView, DeleteCustomerView,
                    updateCustomerView, export_csv, export_pdf)

urlpatterns = [
    url(r'^customer/new/$', createCustomerView, name='new'),
    url(r'^customer/$', CustomerListView.as_view(), name='list'),
    url(r'^customer/delete/(?P<pk>[-\w]+)/$',
        DeleteCustomerView.as_view(), name='delete'),
    url(r'^customer/update/(?P<AccountNum>[-\w]+)/$',
        updateCustomerView, name='update'),
    url(r'^customer/export/cvs/$', export_csv, name='csv'),
    url(r'^customer/export/pdf/$', export_pdf, name='pdf'),
]

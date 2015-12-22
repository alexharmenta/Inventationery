#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:12:26
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-21 20:04:30
from django.conf.urls import url
from .views import (createInventView, InventListView,
                    DeleteInventView, updateInventView,
                    export_csv, export_pdf)

urlpatterns = [
    url(r'^Item/new/$', createInventView, name='new'),
    url(r'^Item/$', InventListView.as_view(), name='list'),
    url(r'^Item/delete/(?P<ItemId>[-\w]+)/$',
        DeleteInventView.as_view(), name='delete'),
    url(r'^Item/update/(?P<ItemId>[-\w]+)/$',
        updateInventView, name='update'),
    url(r'^Item/export/cvs/$', export_csv, name='csv'),
    url(r'^Item/export/pdf/$', export_pdf, name='pdf'),
]

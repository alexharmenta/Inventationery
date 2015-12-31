#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:12:26
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-30 20:18:13
from django.conf.urls import url
from .views import (createInventView, InventListView, InventExistingListView,
                    DeleteInventView, updateInventView,
                    export_csv, export_pdf,
                    CreateLocationView, UpdateLocationView,
                    ListLocationView, DeleteLocationView)

urlpatterns = [
    url(r'^Item/new/$', createInventView, name='new'),
    url(r'^Item/$', InventListView.as_view(), name='list'),
    url(r'^Item/Existing/$', InventExistingListView.as_view(), name='list-existing'),
    url(r'^Item/delete/(?P<ItemId>[-\w]+)/$',
        DeleteInventView.as_view(), name='delete'),
    url(r'^Item/update/(?P<ItemId>[-\w]+)/$',
        updateInventView, name='update'),
    url(r'^Item/export/cvs/$', export_csv, name='csv'),
    url(r'^Item/export/pdf/$', export_pdf, name='pdf'),

    url(r'^Location/new/$', CreateLocationView.as_view(), name='new-location'),
    url(r'^Location/$', ListLocationView.as_view(), name='list-location'),
    url(r'^Location/update/(?P<LocationName>[-\w]+)/$',
        UpdateLocationView.as_view(), name='update-location'),
    url(r'^Location/delete/(?P<LocationName>[-\w]+)/$',
        DeleteLocationView.as_view(), name='delete-location'),
]

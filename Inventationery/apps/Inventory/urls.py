#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:12:26
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-16 19:12:29
from django.conf.urls import url
from .views import (CreateInventView, InventListView,
                    DeleteInventView, UpdateInventView)

urlpatterns = [
    url(r'^Items/new/$', CreateInventView.as_view(), name='new'),
    url(r'^Items/$', InventListView.as_view(), name='list'),
    url(r'^Items/delete/(?P<pk>[-\w]+)/$',
        DeleteInventView.as_view(), name='delete'),
    url(r'^Items/update/(?P<pk>[-\w]+)/$',
        UpdateInventView.as_view(), name='update'),
]

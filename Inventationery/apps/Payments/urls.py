#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-12-20 22:09:47
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-20 22:18:22
from django.conf.urls import url
from .views import (CreatePaymentView,
                    UpdatePaymentView,
                    DeletePaymentView,
                    CreatePaymModeView,
                    UpdatePaymModeView,
                    DeletePaymModeView)

urlpatterns = [
    url(r'^payment/new/$', CreatePaymentView.as_view(), name='new-payment'),
    url(r'^payment/update/(?P<pk>[-\w]+)/$',
        UpdatePaymentView.as_view(), name='update-payment'),
    url(r'^payment/delete/(?P<pk>[-\w]+)/$',
        DeletePaymentView.as_view(), name='delete-payment'),

    url(r'^paym_mode/new/$', CreatePaymModeView.as_view(), name='new-paym'),
    url(r'^paym_mode/update/(?P<pk>[-\w]+)/$',
        UpdatePaymModeView.as_view(), name='update-paym'),
    url(r'^paym_mode/delete/(?P<pk>[-\w]+)/$',
        DeletePaymModeView.as_view(), name='delete-paym'),
]

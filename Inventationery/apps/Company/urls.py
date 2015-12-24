#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmenta
# @Date:   2015-12-24 12:42:57
# @Last Modified by:   harmenta
# @Last Modified time: 2015-12-24 12:44:53
from django.conf.urls import url
from .views import createCompanyInfoView

urlpatterns = [
    url(r'^company/new/$', createCompanyInfoView, name='new'),
]

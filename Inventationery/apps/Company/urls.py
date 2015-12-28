#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmenta
# @Date:   2015-12-24 12:42:57
# @Last Modified by:   harmenta
# @Last Modified time: 2015-12-28 16:01:15
from django.conf.urls import url
from .views import CompanyInfoView

urlpatterns = [
    url(r'^company/$', CompanyInfoView, name='data'),
]

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-14 15:29:52
# @Last Modified by:   harmenta
# @Last Modified time: 2015-12-31 13:22:17
from django.conf.urls import url
from .views import Home
urlpatterns = [
    url(r'^$', Home, name='home'),
]

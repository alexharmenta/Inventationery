#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-14 15:29:52
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-16 18:50:10
from django.conf.urls import url
from .views import TemplateView
urlpatterns = [
    url(r'^$', TemplateView.as_view(), name='home'),
]

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-12-29 23:06:33
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-29 23:07:28
from django.conf.urls import url
from .views import LoginView
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': reverse_lazy('login')}, name='logout'),
]

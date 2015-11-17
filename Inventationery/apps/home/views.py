#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-14 15:29:39
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-16 18:51:25
from django.views.generic import TemplateView
# Create your views here.


class TemplateView(TemplateView):
    template_name = 'home\home.html'

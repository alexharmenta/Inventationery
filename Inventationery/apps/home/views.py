#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-14 15:29:39
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-29 23:04:23
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


class TemplateView(TemplateView):
    template_name = 'home/home.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

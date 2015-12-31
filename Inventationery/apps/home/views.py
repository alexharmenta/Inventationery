#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-14 15:29:39
# @Last Modified by:   harmenta
# @Last Modified time: 2015-12-31 13:31:28
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from Inventationery.apps.Company.models import CompanyInfoModel
# Create your views here.


@login_required
def Home(request):
    try:
        Company = CompanyInfoModel.objects.all()[:1]
    except:
        Company = None

    return render_to_response('home/home.html',
                              {'Company': Company, },
                              context_instance=RequestContext(request))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmenta
# @Date:   2015-12-24 11:10:51
# @Last Modified by:   harmenta
# @Last Modified time: 2015-12-24 13:45:48
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from .models import CompanyInfoModel
from .forms import (CompanyInfoForm, PartyForm, LogisticsPostalForm)
from Inventationery.apps.DirParty.models import DirPartyModel
from Inventationery.apps.LogisticsPostalAddress.models import (
    LogisticsPostalAddressModel)


# FBV: View for create new Company
def createCompanyInfoView(request):
    companyInfo = CompanyInfoModel()
    dirParty = DirPartyModel()
    lpa = LogisticsPostalAddressModel()

    if request.method == 'POST':
        companyInfoForm = CompanyInfoForm(request.POST)
        party_form = PartyForm(request.POST)
        postal_form = LogisticsPostalForm(request.POST)

        if party_form.is_valid():
            dirParty = party_form.save()
            if companyInfoForm.is_valid():
                companyInfo = companyInfoForm.save(commit=False)
                companyInfo.Party = dirParty
                companyInfo.save()

                if postal_form.is_valid():
                    lpa = postal_form.save(commit=False)
                    lpa.Party = dirParty
                    lpa.save()

                messages.success(request, 'Compañía creada correctamente')
        else:
            messages.error(request, 'Revise la información de la compañía')
    else:
        companyInfoForm = CompanyInfoForm()
        party_form = PartyForm()
        postal_form = LogisticsPostalForm()

    return render_to_response('Company/CreateCompanyInfo.html',
                              {'companyInfoForm': companyInfoForm,
                               'party_form': party_form,
                               'postal_form': postal_form, },
                              context_instance=RequestContext(request))

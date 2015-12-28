#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmenta
# @Date:   2015-12-24 11:10:51
# @Last Modified by:   harmenta
# @Last Modified time: 2015-12-28 17:19:56
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from .models import CompanyInfoModel
from .forms import (CompanyInfoForm, PartyForm, LogisticsPostalForm)


# FBV: View for create new Company
def CompanyInfoView(request):
    try:
        Company = CompanyInfoModel.objects.all()[:1].get()
        Party = Company.Party
    except:
        Company = None
        Party = None

    if Company is None:  # Create
        if request.method == 'POST':
            companyInfoForm = CompanyInfoForm(request.POST, request.FILES)
            party_form = PartyForm(request.POST)
            if party_form.is_valid():
                dirParty = party_form.save()
                if companyInfoForm.is_valid():
                    companyInfo = companyInfoForm.save(commit=False)
                    companyInfo.Party = dirParty
                    companyInfo.save()
                messages.success(request, 'Compañía creada correctamente')
            else:
                messages.error(request, 'Revise la información de la compañía')
        else:
            companyInfoForm = CompanyInfoForm()
            party_form = PartyForm()

        return render_to_response('Company/CreateCompanyInfo.html',
                                  {'companyInfoForm': companyInfoForm,
                                   'party_form': party_form, },
                                  context_instance=RequestContext(request))
    else:  # Update
        if request.method == 'POST':
            companyInfoForm = CompanyInfoForm(
                request.POST, request.FILES, instance=Company)
            party_form = PartyForm(request.POST, instance=Party)
            if party_form.is_valid():
                party_form.save()
                if companyInfoForm.is_valid():
                    companyInfo = companyInfoForm.save(commit=False)
                    companyInfo.Party = Party
                    companyInfo.save()
                messages.success(
                    request,
                    'Información de compañía actualizada correctamente')
            else:
                messages.error(request, 'Revise la información de la compañía')
        else:
            companyInfoForm = CompanyInfoForm(instance=Company)
            party_form = PartyForm(instance=Party)
        return render_to_response('Company/UpdateCompanyInfo.html',
                                  {'companyInfoForm': companyInfoForm,
                                   'party_form': party_form,
                                   'Company': Company, },
                                  context_instance=RequestContext(request))

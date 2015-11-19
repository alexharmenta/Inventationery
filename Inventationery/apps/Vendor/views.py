#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:22:12
# @Last Modified by:   harmenta
# @Last Modified time: 2015-11-19 17:25:23
# views.py
from django.shortcuts import render_to_response
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, DeleteView
from .models import VendorModel
from Inventationery.apps.DirParty.models import DirPartyModel
from Inventationery.apps.LogisticsPostalAddress.models import (
    LogisticsPostalAddressModel)
from Inventationery.apps.LogisticsElectronicAddress.models import (
    LogisticsElectronicAddressModel)
from .forms import (VendorForm,
                    PartyForm,)


# CBV: View to list all vendors ordered by AccountNum
# ----------------------------------------------------------------------------
class VendorListView(ListView):
    model = VendorModel
    template_name = 'Vendor/VendorList.html'
    context_object_name = 'vendors'

    def get_queryset(self):
        queryset = super(VendorListView, self).get_queryset()
        queryset = VendorModel.objects.all().order_by('AccountNum')
        return queryset


# FBV: View for create new Vendor
def createVendorView(request):

    ElectronicFormSet = inlineformset_factory(
        DirPartyModel, LogisticsElectronicAddressModel,
        extra=1, max_num=5, fields='__all__')
    PostalFormSet = inlineformset_factory(
        DirPartyModel, LogisticsPostalAddressModel,
        extra=1, max_num=5, fields='__all__')

    if request.method == 'POST':
        # formulario enviado
        vendor_form = VendorForm(request.POST)
        party_form = PartyForm(request.POST)

        electronic_formset = ElectronicFormSet(
            request.POST, prefix='efs')
        postal_formset = PostalFormSet(
            request.POST, prefix='pfs')

        if vendor_form.is_valid() and party_form.is_valid():
            party = party_form.save(commit=False)
            vendor = vendor_form.save(commit=False)
            party.save()
            vendor.Party = party
            vendor.save()

            for electronic_form in electronic_formset:
                if electronic_form.is_valid():
                    description = electronic_form.cleaned_data.get(
                        'Description')
                    contact = electronic_form.cleaned_data.get('Contact')
                    if description and contact:
                        Electronic = electronic_form.save(commit=False)
                        Electronic.Party = party
                        Electronic.save()
                else:
                    party.delete()
                    vendor.delete()

            for postal_form in postal_formset:
                if postal_form.is_valid():
                    description = electronic_form.cleaned_data.get(
                        'Description')
                    if description:
                        Postal = postal_form.save(commit=False)
                        Postal.Party = party
                        Postal.save()
                else:
                    party.delete()
                    vendor.delete()

                redirect_url = "/vendor/update/" + str(vendor.AccountNum)
                return HttpResponseRedirect(redirect_url)

    else:
        # formulario inicial
        vendor_form = VendorForm()
        party_form = PartyForm()
        electronic_formset = ElectronicFormSet(prefix='efs')
        postal_formset = PostalFormSet(prefix='pfs')

    return render_to_response('Vendor/CreateVendor.html',
                              {'vendor_form': vendor_form,
                               'party_form': party_form,
                               'electronic_formset': electronic_formset,
                               'postal_formset': postal_formset, },
                              context_instance=RequestContext(request))


# FBV: View for update an existing Vendor
def updateVendorView(request, AccountNum):

    Vendor = VendorModel.objects.get(AccountNum=AccountNum)

    ElectronicFormSet = inlineformset_factory(
        DirPartyModel, LogisticsElectronicAddressModel,
        extra=1, max_num=5, fields='__all__')
    PostalFormSet = inlineformset_factory(
        DirPartyModel, LogisticsPostalAddressModel,
        extra=1, max_num=5, fields='__all__')

    if request.method == 'POST':
        # formulario enviado
        vendor_form = VendorForm(request.POST, instance=Vendor)
        party_form = PartyForm(request.POST, instance=Vendor.Party)

        electronic_formset = ElectronicFormSet(
            request.POST, prefix='efs', instance=Vendor.Party)
        postal_formset = PostalFormSet(
            request.POST, prefix='pfs', instance=Vendor.Party)

        if vendor_form.is_valid() and party_form.is_valid():
            party = party_form.save()
            vendor = vendor_form.save(commit=False)
            vendor.Party = party

            for electronic_form in electronic_formset.forms:
                if electronic_form.is_valid():
                    description = electronic_form.cleaned_data.get(
                        'Description')
                    contact = electronic_form.cleaned_data.get('Contact')
                    if description and contact:
                        electronic = electronic_form.save(commit=False)
                        electronic.Party = party

            for postal_form in postal_formset:
                if postal_form.is_valid():
                    description = electronic_form.cleaned_data.get(
                        'Description')
                    if description:
                        postal = postal_form.save(commit=False)
                        postal.Party = party
                        postal.save()

    else:
        # formulario inicial
        vendor_form = VendorForm(instance=Vendor)
        party_form = PartyForm(instance=Vendor.Party)
        electronic_formset = ElectronicFormSet(
            prefix='efs', instance=Vendor.Party)
        postal_formset = PostalFormSet(
            prefix='pfs', instance=Vendor.Party)

    return render_to_response('Vendor/VendorDetail.html',
                              {'vendor_form': vendor_form,
                               'party_form': party_form,
                               'electronic_formset': electronic_formset,
                               'postal_formset': postal_formset,
                               'Vendor': Vendor, },
                              context_instance=RequestContext(request))


# CBV: View to delete an existing vendor
# ----------------------------------------------------------------------------
class DeleteVendorView(DeleteView):
    model = VendorModel
    template_name = 'Vendor/DeleteVendor.html'
    success_url = '/vendor'
    success_message = 'Proveedor eliminado correctamente'

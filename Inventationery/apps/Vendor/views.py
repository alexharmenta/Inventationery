#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:22:12
# @Last Modified by:   harmenta
# @Last Modified time: 2015-11-18 17:46:39
# views.py
from django.shortcuts import render_to_response
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, DeleteView, UpdateView
from .models import VendorModel
from Inventationery.apps.DirParty.models import DirPartyModel
from Inventationery.apps.LogisticsPostalAddress.models import (
    LogisticsPostalAddressModel)
from Inventationery.apps.LogisticsElectronicAddress.models import (
    LogisticsElectronicAddressModel)
from .forms import (VendorForm,
                    PartyForm,)


class VendorList(ListView):
    model = VendorModel
    template_name = 'Vendor/VendorList.html'
    context_object_name = 'vendors'

    def get_queryset(self):
        queryset = super(VendorList, self).get_queryset()
        queryset = VendorModel.objects.all().order_by('AccountNum')
        return queryset


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

        postal_formset = PostalFormSet(request.POST, prefix='pfs')
        electronic_formset = ElectronicFormSet(request.POST, prefix='efs')

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


class DeleteVendorView(DeleteView):
    model = VendorModel
    template_name = 'Vendor/DeleteVendor.html'
    success_url = '/vendor'
    success_message = 'Proveedor eliminado correctamente'


class UpdateVendorView(UpdateView):
    form_class = VendorForm
    template_name = 'Vendor/VendorDetail.html'
    model = VendorModel
    slug_field = 'AccountNum'
    slug_url_kwarg = 'AccountNum'

    ElectronicFormSet = inlineformset_factory(
        DirPartyModel, LogisticsElectronicAddressModel,
        extra=1, max_num=5, fields='__all__')
    PostalFormSet = inlineformset_factory(
        DirPartyModel, LogisticsPostalAddressModel,
        extra=1, max_num=5, fields='__all__')

    def get_context_data(self, **kwargs):
        context = super(UpdateVendorView, self).get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return self.request.path

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        vendor_form = self.get_form()
        Vend = VendorModel.objects.get(AccountNum=kwargs['AccountNum'])
        Party = Vend.Party
        party_form = PartyForm(instance=Party)

        electronic_formset = self.ElectronicFormSet(
            instance=Party, prefix='efs')
        postal_formset = self.PostalFormSet(instance=Party, prefix='pfs')

        return render_to_response('Vendor/VendorDetail.html',
                                  {'vendor_form': vendor_form,
                                      'party_form': party_form,
                                      'electronic_formset': electronic_formset,
                                      'postal_formset': postal_formset,
                                   },
                                  context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.context = self.get_context_data()

        vendor_form = self.get_form()
        party_form = PartyForm(request.POST, instance=self.object.Party)

        if vendor_form.is_valid() and party_form.is_valid():
            vendor_form.save()
            Party = party_form.save(commit=False)
            Party.save()

            electronic_formset = self.ElectronicFormSet(
                request.POST, instance=Party, prefix='efs')
            postal_formset = self.PostalFormSet(
                request.POST, instance=Party, prefix='pfs')

            for electronic_form in electronic_formset:
                if electronic_form.is_valid():
                    electronic_form.save()

            for postal_form in postal_formset:
                if postal_form.is_valid():
                    postal_form.save()

        return render_to_response('Vendor/VendorDetail.html',
                                  {'vendor_form': vendor_form,
                                      'party_form': party_form,
                                      'electronic_formset': electronic_formset,
                                      'postal_formset': postal_formset,
                                   },
                                  context_instance=RequestContext(request))

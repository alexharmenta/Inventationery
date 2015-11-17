#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:22:12
# @Last Modified by:   harmenta
# @Last Modified time: 2015-11-17 17:51:10
# views.py
from django.shortcuts import render_to_response
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, DeleteView, UpdateView
from .models import VendorModel
from Inventationery.apps.LogisticsPostalAddress.models import (
    LogisticsPostalAddressModel)
from Inventationery.apps.LogisticsElectronicAddress.models import (
    LogisticsElectronicAddressModel)
from .forms import (VendorForm,
                    PartyForm,
                    LogisticsPostalForm,
                    LogisticsElectronicForm,
                    BasePostalFormSet,
                    BaseElectronicFormSet)


class VendorList(ListView):
    model = VendorModel
    template_name = 'Vendor/VendorList.html'
    context_object_name = 'vendors'

    def get_queryset(self):
        queryset = super(VendorList, self).get_queryset()
        queryset = VendorModel.objects.all().order_by('AccountNum')
        return queryset


def createVendorView(request):

    PostalFormSet = formset_factory(
        LogisticsPostalForm, formset=BasePostalFormSet, extra=1, max_num=5)
    ElectronicFormSet = formset_factory(
        LogisticsElectronicForm,
        formset=BaseElectronicFormSet,
        extra=1,
        max_num=5)

    if request.method == 'POST':
        # formulario enviado
        vendor_form = VendorForm(request.POST)
        party_form = PartyForm(request.POST)

        postal_formset = PostalFormSet(request.POST, prefix='pfs')
        electronic_formset = ElectronicFormSet(request.POST, prefix='efs')

        vendor_valid = False
        party_valid = False
        postal_valid = False
        electronic_valid = False

        if vendor_form.is_valid() and party_form.is_valid():
            vendor_valid = True
            party_valid = True
            
            Party = party_form.save()
            vendor = vendor_form.save(commit=False)
            vendor.Party = Party
            vendor.save()

            if postal_formset.is_valid():
                for postal_form in postal_formset:
                    if postal_form.is_valid():
                        Postal = postal_form.save(commit=False)
                        Postal.Party = Party
                        Postal.save()
                        postal_valid = True
                    else:
                        Party.delete()
                        vendor.delete()
                        postal_valid = False
            else:
                Party.delete()
                vendor.delete()
                postal_valid = False

            if electronic_formset.is_valid():
                for electronic_form in electronic_formset:
                    if electronic_form.is_valid():
                        Electronic = electronic_form.save(commit=False)
                        Electronic.Party = Party
                        Electronic.save()
                        electronic_valid = True
                    else:
                        Party.delete()
                        vendor.delete()
                        electronic_valid = False
            else:
                Party.delete()
                vendor.delete()
                electronic_valid = False


        if vendor_valid and party_valid and postal_valid and electronic_valid:
            redirect_url = "/vendor/update/" + str(vendor.pk)
            return HttpResponseRedirect(redirect_url)

    else:
        # formulario inicial
        vendor_form = VendorForm()
        party_form = PartyForm()
        postal_formset = PostalFormSet(prefix='pfs')
        electronic_formset = ElectronicFormSet(prefix='efs')

    return render_to_response('Vendor/CreateVendor.html',
                              {'vendor_form': vendor_form,
                               'party_form': party_form,
                               'postal_formset': postal_formset,
                               'electronic_formset': electronic_formset, },
                              context_instance=RequestContext(request))


class DeleteVendorView(DeleteView):
    model = VendorModel
    template_name = 'Vendor/DeleteVendor.html'
    success_url = '/vendor'
    success_message = 'Proveedor eliminado correctamente'


class UpdateVendorView(UpdateView):
    form_class = VendorForm
    template_name = 'Vendor/VendorDetails.html'
    model = VendorModel

    def get_context_data(self, **kwargs):
        context = super(UpdateVendorView, self).get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return self.request.path

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        vendor_form = self.get_form()
        Vend = VendorModel.objects.get(pk=kwargs['pk'])
        Party = Vend.Party
        party_form = PartyForm(instance=Party)

        PostalFormSet = formset_factory(
            LogisticsPostalForm,
            formset=BasePostalFormSet,
            extra=1,
            max_num=5,
            can_delete=True)
        ElectronicFormSet = formset_factory(
            LogisticsElectronicForm,
            formset=BaseElectronicFormSet,
            extra=1,
            max_num=5,
            can_delete=True)

        postal_addresses = LogisticsPostalAddressModel.objects.filter(
            Party=Party).order_by('-IsPrimary')
        postal_data = [{'Description': p.Description,
                        'Purpose': p.Purpose,
                        'CountryRegionId': p.CountryRegionId,
                        'ZipCode': p.ZipCode,
                        'Street': p.Street,
                        'StreetNumber': p.StreetNumber,
                        'BuildingCompliment': p.BuildingCompliment,
                        'City': p.City,
                        'State': p.State,
                        'IsPrimary': p.IsPrimary,
                        'Party': p.Party, }
                       for p in postal_addresses]
        postal_formset = PostalFormSet(initial=postal_data, prefix='pfs')

        electronic_addresses = LogisticsElectronicAddressModel.objects.filter(
            Party=Party).order_by('-IsPrimary')
        electronic_data = [{'Description': e.Description,
                            'Type': e.Type,
                            'Contact': e.Contact,
                            'IsPrimary': e.IsPrimary,
                            'Party': e.Party, }
                           for e in electronic_addresses]
        electronic_formset = ElectronicFormSet(
            initial=electronic_data, prefix='efs')

        return render_to_response('Vendor/VendorDetails.html',
                                  {'vendor_form': vendor_form,
                                      'party_form': party_form,
                                      'postal_formset': postal_formset,
                                      'electronic_formset': electronic_formset,
                                   },
                                  context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.context = self.get_context_data()
        vendor_form = self.get_form()
        Vend = VendorModel.objects.get(pk=kwargs['pk'])
        Party = Vend.Party
        party_form = PartyForm(request.POST, instance=Party)
        valid = True

        PostalFormSet = formset_factory(
            LogisticsPostalForm, formset=BasePostalFormSet)
        ElectronicFormSet = formset_factory(
            LogisticsElectronicForm, formset=BaseElectronicFormSet)

        postal_formset = PostalFormSet(request.POST, prefix='pfs')
        electronic_formset = ElectronicFormSet(request.POST, prefix='efs')

        if vendor_form.is_valid() and party_form.is_valid():
            Party = party_form.save(commit=False)
            Party.save()
            vendor = vendor_form.save(commit=False)
            vendor.Party = Party
            vendor.save()

            for postal_form in postal_formset:
                if postal_form.is_valid():
                    valid = True
                else:
                    valid = False
                    break
            if valid:
                LogisticsPostalAddressModel.objects.filter(
                    Party=Party).delete()
                for postal_form in postal_formset:
                    description = postal_form.cleaned_data.get(
                        'Description')
                    if description:
                        Postal = postal_form.save(commit=False)
                        Postal.Party = Party
                        Postal.save()

            for electronic_form in electronic_formset:
                if electronic_form.is_valid():
                    valid = True
                else:
                    valid = False
                    break
            if valid:
                LogisticsElectronicAddressModel.objects.filter(
                    Party=Party).delete()
                for electronic_form in electronic_formset:
                    description = electronic_form.cleaned_data.get(
                        'Description')
                    contact = electronic_form.cleaned_data.get('Contact')
                    if description and contact:
                        Electronic = electronic_form.save(commit=False)
                        Electronic.Party = Party
                        Electronic.save()
        redirect_url = "/vendor/update/" + str(vendor.pk)
        return HttpResponseRedirect(redirect_url)

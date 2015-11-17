#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:15:59
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-16 20:05:25
# from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.forms.formsets import formset_factory
from django.http import JsonResponse
from .models import PurchOrderModel
from .forms import PurchOrderForm, PurchOrderLinesForm, BasePurchLineFormSet
from Inventationery.apps.Vendor.models import VendModel
from Inventationery.apps.Inventory.models import InventModel
# Create your views here.


class PurchOrderListView(ListView):
    model = PurchOrderModel
    template_name = 'PurchOrder/PurchOrderList.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super(PurchOrderListView, self).get_queryset()
        queryset = PurchOrderModel.objects.all().order_by('PurchId')
        return queryset


class PurchOrderCreateView(CreateView):
    model = PurchOrderModel
    form_class = PurchOrderForm
    template_name = 'PurchOrder/PurchOrderCreate.html'
    success_url = '/purch_orders'

    PurchLineFormset = formset_factory(
        PurchOrderLinesForm, formset=BasePurchLineFormSet)

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates a blank version of the form.
        """
        self.object = None
        purch_form = self.get_form()
        purchline_formset = self.PurchLineFormset(prefix='plfs')
        return self.render_to_response(
            self.get_context_data(purch_form=purch_form,
                                  purchline_formset=purchline_formset))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        if self.request.is_ajax():
            action = request.POST.get('action', '')
            if action == 'get_purch_data':
                AccountNum = request.POST.get('AccountNum', '')
                try:
                    Vendor = VendModel.objects.get(AccountNum=AccountNum)
                    response_dict = {
                        'NameAlias': Vendor.Party.NameAlias,
                        'VATNum': Vendor.VATNum,
                        'CurrencyCode': Vendor.CurrencyCode,
                        'LanguageCode': Vendor.Party.LanguageCode,
                        'OneTimeVendor': Vendor.OneTimeVendor,
                        'DeliveryName': Vendor.get_PrimaryAddress(),
                    }
                except:
                    response_dict = {
                        'Name': '',
                        'VATNum': '',
                        'CurrencyCode': '',
                        'LanguageCode': '',
                        'OneTimeVendor': '',
                        'DeliveryName': '',
                    }
            elif action == 'get_purchline_data':
                ItemId = request.POST.get('ItemId', '')
                try:
                    Invent = InventModel.objects.get(ItemId=ItemId)
                    response_dict = {
                        'ItemName': Invent.ItemName,
                        'UnitId': Invent.UnitId,
                        'VendorPrice': Invent.VendorPrice,
                    }
                except:
                    response_dict = {
                        'ItemName': '',
                        'UnitId': '',
                        'VendorPrice': '',
                    }

            return JsonResponse(response_dict)

        self.object = None
        self.context = self.get_context_data()

        purch_form = self.get_form()
        purchline_formset = self.PurchLineFormset(request.POST, prefix='plfs')

        if purch_form.is_valid():

            purch_form.save()

            for purchline_form in purchline_formset:
                if purchline_form.is_valid():
                    purchline_form.save(commit=False)
                    purchline_form.PurchOrder = purch_form
                    purchline_form.save()

            return self.form_valid(self, purch_form)
        else:
            return self.form_invalid(purch_form)

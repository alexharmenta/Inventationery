#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:15:59
# @Last Modified by:   harmenta
# @Last Modified time: 2015-11-19 17:50:34
# from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView
from django.forms import inlineformset_factory
from django.http import JsonResponse
from .models import PurchOrderModel, PurchLineModel
from .forms import PurchOrderForm
from Inventationery.apps.Vendor.models import VendorModel
from Inventationery.apps.Inventory.models import InventModel
# Create your views here.


# CBV: View to list all PurchOrders ordered by created
# ----------------------------------------------------------------------------
class PurchOrderListView(ListView):
    model = PurchOrderModel
    template_name = 'PurchOrder/PurchOrderList.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super(PurchOrderListView, self).get_queryset()
        queryset = PurchOrderModel.objects.all().order_by('created')
        return queryset


# FBV: View for create new Purchase Orders
def createPurchOrderView(request):

    PurchLineFormset = inlineformset_factory(
        PurchOrderModel, PurchLineModel, extra=1, fields='__all__')

    if request.method == 'POST':

        purch_form = PurchOrderForm(request.POST)
        purchline_formset = PurchLineFormset(request.POST, prefix='plfs')

        if purch_form.is_valid():
            PurchOrder = purch_form.save()

            for purchline_form in purchline_formset:
                if purchline_form.is_valid():
                    purchline_form.save(commit=False)
                    purchline_form.PurchOrder = PurchOrder
                    purchline_form.save()

            redirect_url = "/purch_orders/update/" + str(PurchOrder.PurchId)
            return HttpResponseRedirect(redirect_url)

        # Get info to retrieve to template with Ajax
        if request.is_ajax():
            action = request.POST.get('action', '')
            if action == 'get_purch_data':
                AccountNum = request.POST.get('AccountNum', '')
                try:
                    print 'try'
                    Vendor = VendorModel.objects.get(AccountNum=AccountNum)
                    response_dict = {
                        'NameAlias': Vendor.Party.NameAlias,
                        'VATNum': Vendor.VATNum,
                        'CurrencyCode': Vendor.CurrencyCode,
                        'LanguageCode': Vendor.Party.LanguageCode,
                        'OneTimeVendor': Vendor.OneTimeVendor,
                        'DeliveryName': Vendor.get_PrimaryAddress(),
                    }
                except:
                    print 'except'
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

    else:
        purch_form = PurchOrderForm()
        purchline_formset = PurchLineFormset(prefix='plfs')

    return render_to_response('PurchOrder/PurchOrderCreate.html',
                              {'purch_form': purch_form,
                               'purchline_formset': purchline_formset},
                              context_instance=RequestContext(request))


# FBV: View for update new Purchase Orders
def updatePurchOrderView(request, PurchId):
    PurchOrder = get_object_or_404(PurchOrderModel, PurchId=PurchId)
    PurchLineFormset = inlineformset_factory(
        PurchOrderModel, PurchLineModel, extra=1, fields='__all__')

    if request.method == 'POST':

        purch_form = PurchOrderForm(request.POST)
        purchline_formset = PurchLineFormset(request.POST, prefix='plfs')

        if purch_form.is_valid():
            PurchOrder = purch_form.save()

            for purchline_form in purchline_formset:
                if purchline_form.is_valid():
                    purchline_form.save(commit=False)
                    purchline_form.PurchOrder = PurchOrder
                    purchline_form.save()

            return HttpResponseRedirect('/purch_orders/')

        # Get info to retrieve to template with Ajax
        if request.is_ajax():
            action = request.POST.get('action', '')
            if action == 'get_purch_data':
                AccountNum = request.POST.get('AccountNum', '')
                try:
                    print 'try'
                    Vendor = VendorModel.objects.get(AccountNum=AccountNum)
                    response_dict = {
                        'NameAlias': Vendor.Party.NameAlias,
                        'VATNum': Vendor.VATNum,
                        'CurrencyCode': Vendor.CurrencyCode,
                        'LanguageCode': Vendor.Party.LanguageCode,
                        'OneTimeVendor': Vendor.OneTimeVendor,
                        'DeliveryName': Vendor.get_PrimaryAddress(),
                    }
                except:
                    print 'except'
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

    else:
        purch_form = PurchOrderForm(instance=PurchOrder)
        purchline_formset = PurchLineFormset(
            instance=PurchOrder, prefix='plfs')

    return render_to_response('PurchOrder/PurchOrderCreate.html',
                              {'purch_form': purch_form,
                               'purchline_formset': purchline_formset},
                              context_instance=RequestContext(request))

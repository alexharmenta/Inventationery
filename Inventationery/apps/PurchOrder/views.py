#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:15:59
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-12 15:21:09
# from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, DeleteView
from django.forms import inlineformset_factory
from django.http import JsonResponse
from datetime import date
from .models import PurchOrderModel, PurchLineModel
from .forms import PurchOrderForm, PurchOrderLinesForm
from Inventationery.apps.Vendor.models import VendorModel
from Inventationery.apps.Inventory.models import (ItemModel, InventoryModel)
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
        PurchOrderModel,
        PurchLineModel,
        extra=1,
        fields='__all__',
        form=PurchOrderLinesForm)

    if request.method == 'POST':

        purch_form = PurchOrderForm(request.POST)
        purchline_formset = PurchLineFormset(
            request.POST, prefix='plfs')

        # Get info to retrieve to template with Ajax
        if request.is_ajax():
            action = request.POST.get('action', '')
            if action == 'get_purch_data':
                Vendor_pk = request.POST.get('Vendor_pk', '')
                try:
                    Vendor = VendorModel.objects.get(pk=Vendor_pk)
                    response_dict = {
                        'NameAlias': Vendor.Party.NameAlias,
                        'VATNum': Vendor.VATNum,
                        'CurrencyCode': Vendor.CurrencyCode,
                        'LanguageCode': Vendor.Party.LanguageCode,
                        'OneTimeVendor': Vendor.OneTimeVendor,
                        'DeliveryName': Vendor.get_PrimaryAddress(),
                        'DeliveryContact': Vendor.get_PrimaryElectronic(),
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
                Item_pk = request.POST.get('Item_pk', '')
                try:
                    Invent = ItemModel.objects.get(pk=Item_pk)
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

        if purch_form.is_valid():
            PurchOrder = purch_form.save()
            messages.success(request, "Orden de compra creada correctamente")

            purchline_formset = PurchLineFormset(
                request.POST, instance=PurchOrder, prefix='plfs')

            for purchline_form in purchline_formset:
                if purchline_form.is_valid():
                    itemid = purchline_form.cleaned_data.get('ItemId')
                    if itemid:
                        purchline_form.save()
                else:
                    messages.warning(
                        request,
                        'Revise la información de las lineas de la OC')

            redirect_url = "/purch_orders/update/" + str(PurchOrder.PurchId)
            return HttpResponseRedirect(redirect_url)
        else:
            purchline_formset = PurchLineFormset(request.POST, prefix='plfs')
            messages.error(
                request, "Ocurrió un error al crear la orden de compra")

    else:
        purch_form = PurchOrderForm(initial={'Enabled': True})
        purchline_formset = PurchLineFormset(prefix='plfs')
    return render_to_response('PurchOrder/CreatePurchOrder.html',
                              {'purch_form': purch_form,
                               'purchline_formset': purchline_formset,
                               'Today': date.today(), },
                              context_instance=RequestContext(request))


# FBV: View for update new Purchase Orders
def updatePurchOrderView(request, PurchId):
    PurchOrder = get_object_or_404(PurchOrderModel, PurchId=PurchId)
    PL_list = []

    PurchLineFormset = inlineformset_factory(
        PurchOrderModel,
        PurchLineModel,
        extra=1,
        fields='__all__',
        form=PurchOrderLinesForm)

    if request.method == 'POST':
        purch_form = PurchOrderForm(request.POST, instance=PurchOrder)
        purchline_formset = PurchLineFormset(
            request.POST, instance=PurchOrder, prefix='plfs')
        # Get info to retrieve to template with Ajax
        if request.is_ajax():
            action = request.POST.get('action', '')
            if action == 'get_purch_data':
                Vendor_pk = request.POST.get('Vendor_pk', '')
                try:
                    Vendor = VendorModel.objects.get(pk=Vendor_pk)
                    response_dict = {
                        'NameAlias': Vendor.Party.NameAlias,
                        'VATNum': Vendor.VATNum,
                        'CurrencyCode': Vendor.CurrencyCode,
                        'LanguageCode': Vendor.Party.LanguageCode,
                        'OneTimeVendor': Vendor.OneTimeVendor,
                        'DeliveryName': Vendor.get_PrimaryAddress(),
                        'DeliveryContact': Vendor.get_PrimaryElectronic(),
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
                Item_pk = request.POST.get('Item_pk', '')
                try:
                    Invent = ItemModel.objects.get(pk=Item_pk)
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
            elif action == 'update_enabled':
                enable = request.POST.get('purch_enabled', '')
                if enable == 'true':
                    enable = True
                    PurchOrderModel.objects.filter(pk=PurchOrder.pk).update(
                        Enabled=enable, PurchStatus='OPE')
                else:
                    enable = False
                    PurchOrderModel.objects.filter(pk=PurchOrder.pk).update(
                        Enabled=enable, PurchStatus='CAN')

                response_dict = {'PurchOrder': PurchOrder.PurchId, }
                return JsonResponse(response_dict)
            elif action == 'receive_pay':
                if purch_form.is_valid():
                    PurchOrder = purch_form.save(commit=False)
                    PurchOrder.PurchStatus = 'RPA'
                    PurchOrder.Enabled = False
                    PurchOrder.save()

                    for purchline_form in purchline_formset:
                        if purchline_form.is_valid():
                            itemid = purchline_form.cleaned_data.get('ItemId')
                            qty = purchline_form.cleaned_data.get('PurchQty')
                            if itemid and qty:
                                PurchLine = purchline_form.save()
                                PL_list.append(PurchLine.pk)
                                try:
                                    Item = ItemModel.objects.get(ItemId=itemid)
                                    Inventory = InventoryModel.objects.get(
                                        Item=Item,
                                        Location=PurchOrder.Location)
                                    if (Inventory.Qty == 0 or
                                            Inventory.Qty is None):
                                        Inventory.Qty = qty
                                    else:
                                        Inventory.Qty += qty
                                    Inventory.save()
                                except:
                                    InventoryModel.objects.create(
                                        Item=Item,
                                        Qty=qty,
                                        Location=PurchOrder.Location)
                        else:
                            messages.warning(
                                request,
                                'Revise la información de las lineas de la OC')
                else:
                    purchline_formset = PurchLineFormset(
                        request.POST, prefix='plfs')
                    messages.error(
                        request, "Ocurrió un error al registrar la recepción")

                return render_to_response(
                    'PurchOrder/UpdatePurchOrder.html',
                    {
                        'purch_form': purch_form,
                        'purchline_formset': purchline_formset,
                        'PurchOrder': PurchOrder
                    },
                    context_instance=RequestContext(request)
                )
            elif action == 'pay_order':
                if purch_form.is_valid():
                    purchStatus = purch_form.cleaned_data.get('PurchStatus')
                    PurchOrder = purch_form.save(commit=False)
                    if purchStatus == 'REC':
                        PurchOrder.PurchStatus = 'RPA'
                        PurchOrder.Enabled = False
                    else:
                        PurchOrder.PurchStatus = 'PAI'

                    PurchOrder.save()

                    for purchline_form in purchline_formset:
                        if purchline_form.is_valid():
                            itemid = purchline_form.cleaned_data.get('ItemId')
                            if itemid:
                                PurchLine = purchline_form.save()
                                PL_list.append(PurchLine.pk)
                    response_dict = {
                        'Enabled': PurchOrder.Enabled,
                        'PurchStatus': PurchOrder.PurchStatus,
                    }

                    return JsonResponse(response_dict)
                else:
                    purchline_formset = PurchLineFormset(
                        request.POST, prefix='plfs')
                    messages.error(
                        request, "Ocurrió un error al registrar la recepción")
                    return render_to_response(
                        'PurchOrder/UpdatePurchOrder.html',
                        {'purch_form': purch_form,
                         'purchline_formset': purchline_formset,
                         'PurchOrder': PurchOrder},
                        context_instance=RequestContext(request))
            elif action == 'receive':
                if purch_form.is_valid():
                    purchStatus = purch_form.cleaned_data.get('PurchStatus')
                    PurchOrder = purch_form.save(commit=False)
                    if purchStatus == 'PAI':
                        PurchOrder.PurchStatus = 'RPA'
                        PurchOrder.Enabled = False
                    else:
                        PurchOrder.PurchStatus = 'REC'

                    PurchOrder.save()

                    for purchline_form in purchline_formset:
                        if purchline_form.is_valid():
                            itemid = purchline_form.cleaned_data.get('ItemId')
                            qty = purchline_form.cleaned_data.get('PurchQty')
                            if itemid and qty:
                                PurchLine = purchline_form.save()
                                PL_list.append(PurchLine.pk)
                                try:
                                    Item = ItemModel.objects.get(ItemId=itemid)
                                    Inventory = InventoryModel.objects.get(
                                        Item=Item,
                                        Location=PurchOrder.Location)
                                    if (Inventory.Qty == 0 or
                                            Inventory.Qty is None):
                                        Inventory.Qty = qty
                                    else:
                                        Inventory.Qty += qty
                                    Inventory.save()
                                    messages.success(
                                        request,
                                        "Artículos recibidos")
                                except:
                                    InventoryModel.objects.create(
                                        Item=Item,
                                        Qty=qty,
                                        Location=PurchOrder.Location)
                        else:
                            messages.warning(
                                request,
                                'Revise la información de las lineas de la OC')
                    response_dict = {
                        'Enabled': PurchOrder.Enabled,
                        'PurchStatus': PurchOrder.PurchStatus,
                    }
                    return JsonResponse(response_dict)
                else:
                    purchline_formset = PurchLineFormset(
                        request.POST, prefix='plfs')
                    messages.error(
                        request, "Ocurrió un error al registrar la recepción")

                    return render_to_response(
                        'PurchOrder/UpdatePurchOrder.html',
                        {
                            'purch_form': purch_form,
                            'purchline_formset': purchline_formset,
                            'PurchOrder': PurchOrder
                        },
                        context_instance=RequestContext(request)
                    )

            return JsonResponse(response_dict)

        if purch_form.is_valid():
            purch_form.save()
            messages.success(request, "Orden de compra actualizada")

            for purchline_form in purchline_formset:
                if purchline_form.is_valid():
                    itemid = purchline_form.cleaned_data.get('ItemId')
                    if itemid:
                        PL = purchline_form.save()
                        PL_list.append(PL.pk)
                else:
                    messages.warning(
                        request,
                        'Revise la información de las lineas de la OC')
        else:
            purchline_formset = PurchLineFormset(request.POST, prefix='plfs')
            messages.error(
                request, "Ocurrió un error al crear la orden de compra")

        if purchline_formset.is_valid():
            PurchLineModel.objects.exclude(pk__in=list(PL_list)).delete()

    else:
        purch_form = PurchOrderForm(instance=PurchOrder)
        purchline_formset = PurchLineFormset(
            instance=PurchOrder, prefix='plfs',)

    return render_to_response('PurchOrder/UpdatePurchOrder.html',
                              {'purch_form': purch_form,
                               'purchline_formset': purchline_formset,
                               'PurchOrder': PurchOrder},
                              context_instance=RequestContext(request))


# CBV: View to delete an existing Purchase order
# ----------------------------------------------------------------------------
class DeletePurchOrderView(DeleteView):
    model = PurchOrderModel
    template_name = 'PurchOrder/DeletePurchOrder.html'
    success_url = '/purch_orders'
    success_message = 'Se ha eliminado la orden de compra'

    def delete(self, request, *args, **kwargs):
        """
        Calls the delete() method on the fetched object and then
        redirects to the success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request,
                         "Se ha eliminado la orden de compra",
                         extra_tags='msg')
        return HttpResponseRedirect(success_url)

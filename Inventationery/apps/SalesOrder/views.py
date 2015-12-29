#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:15:59
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-28 23:59:55
# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.views.generic import ListView, DeleteView
from django.forms import inlineformset_factory
from django.http import JsonResponse
import csv
import time
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from datetime import date
from .models import SalesOrderModel, SalesLineModel
from .forms import SalesOrderForm, SalesOrderLinesForm
from Inventationery.apps.Customer.models import CustomerModel
from Inventationery.apps.Inventory.models import (
    ItemModel, InventoryModel, EcoResProductModel)
# Create your views here.


# CBV: View to list all SalesOrders ordered by created
# ----------------------------------------------------------------------------
class SalesOrderListView(ListView):
    model = SalesOrderModel
    template_name = 'SalesOrder/SalesOrderList.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super(SalesOrderListView, self).get_queryset()
        queryset = SalesOrderModel.objects.all().order_by('created')
        return queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


# CBV: View to list recent 10 SalesOrders ordered by created
# ----------------------------------------------------------------------------
class SalesOrderRecentListView(ListView):
    model = SalesOrderModel
    template_name = 'SalesOrder/SalesOrderRecentList.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super(SalesOrderRecentListView, self).get_queryset()
        queryset = SalesOrderModel.objects.reverse().order_by('created')[:10]
        return queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


# CBV: View to list open SalesOrders ordered by created
# ----------------------------------------------------------------------------
class SalesOrderOpenListView(ListView):
    model = SalesOrderModel
    template_name = 'SalesOrder/SalesOrderOpenList.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super(SalesOrderOpenListView, self).get_queryset()
        queryset = SalesOrderModel.objects.filter(
            Q(SalesStatus='OPE') |
            Q(SalesStatus='RED') |
            Q(SalesStatus='CAS')).order_by('created')
        return queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


# CBV: View to list reduced SalesOrders ordered by created
# ----------------------------------------------------------------------------
class SalesOrderSentListView(ListView):
    model = SalesOrderModel
    template_name = 'SalesOrder/SalesOrderSentList.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super(SalesOrderSentListView, self).get_queryset()
        queryset = SalesOrderModel.objects.filter(
            Q(SalesStatus='RED') |
            Q(SalesStatus='RCA')).order_by('created')
        return queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


# CBV: View to list paid SalesOrders ordered by created
# ----------------------------------------------------------------------------
class SalesOrderChargedListView(ListView):
    model = SalesOrderModel
    template_name = 'SalesOrder/SalesOrderChargedList.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super(SalesOrderChargedListView, self).get_queryset()
        queryset = SalesOrderModel.objects.filter(
            Q(SalesStatus='CAS') |
            Q(SalesStatus='RCA')).order_by('created')
        return queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


# FBV: View for create new Sales Orders
@login_required
def createSalesOrderView(request):
    SalesLineFormset = inlineformset_factory(
        SalesOrderModel,
        SalesLineModel,
        extra=1,
        fields='__all__',
        form=SalesOrderLinesForm)

    if request.method == 'POST':
        sales_form = SalesOrderForm(request.POST)
        salesline_formset = SalesLineFormset(
            request.POST, prefix='slfs')

        # Get info to retrieve to template with Ajax
        if request.is_ajax():
            action = request.POST.get('action', '')
            if action == 'get_sales_data':
                Customer_pk = request.POST.get('Customer_pk', '')
                response_dict = GetCustomerInfo(Customer_pk)
            elif action == 'get_salesline_data':
                Item_pk = request.POST.get('Item_pk', '')
                response_dict = GetLineInfo(Item_pk)
            return JsonResponse(response_dict)

        if sales_form.is_valid():
            SalesOrder = sales_form.save()
            messages.success(request, "Orden de venta creada correctamente")

            salesline_formset = SalesLineFormset(
                request.POST, instance=SalesOrder, prefix='slfs')

            for salesline_form in salesline_formset:
                if salesline_form.is_valid():
                    itemid = salesline_form.cleaned_data.get('ItemId')
                    if itemid:
                        salesline_form.save()
                else:
                    messages.warning(
                        request,
                        'Revise la información de las lineas de la OV')

            redirect_url = "/sales_orders/update/" + str(SalesOrder.SalesId)
            return HttpResponseRedirect(redirect_url)
        else:
            salesline_formset = SalesLineFormset(request.POST, prefix='slfs')
            messages.error(
                request, "Ocurrió un error al crear la orden de venta")

    else:
        sales_form = SalesOrderForm(initial={'Enabled': True})
        salesline_formset = SalesLineFormset(prefix='slfs')
    return render_to_response('SalesOrder/CreateSalesOrder.html',
                              {'sales_form': sales_form,
                               'salesline_formset': salesline_formset,
                               'Today': date.today(), },
                              context_instance=RequestContext(request))


# FBV: View for update new Sales Orders
@login_required
def updateSalesOrderView(request, SalesId):
    SalesOrder = get_object_or_404(SalesOrderModel, SalesId=SalesId)
    SL_list = []
    SalesLineFormset = inlineformset_factory(
        SalesOrderModel,
        SalesLineModel,
        extra=1,
        fields='__all__',
        form=SalesOrderLinesForm)

    if request.method == 'POST':
        sales_form = SalesOrderForm(request.POST, instance=SalesOrder)
        salesline_formset = SalesLineFormset(
            request.POST, instance=SalesOrder, prefix='slfs')
        # Get info to retrieve to template with Ajax
        if request.is_ajax():
            action = request.POST.get('action', '')
            if action == 'get_sales_data':
                Customer_pk = request.POST.get('Customer_pk', '')
                response_dict = GetCustomerInfo(Customer_pk)
            elif action == 'get_salesline_data':
                Item_pk = request.POST.get('Item_pk', '')
                response_dict = GetLineInfo(Item_pk)
            elif action == 'update_enabled':
                if sales_form.is_valid():
                    SalesOrder = sales_form.save(commit=False)
                    enabled = request.POST.get('sales_enabled', '')
                    if (enabled == 'true' and
                            SalesOrder.DocumentState == 'Abierto'):
                        SalesOrder.SalesStatus = 'CAN'
                        SalesOrder.DocumentState = 'Cerrado'
                        SalesOrder.Enabled = False
                    elif (enabled == 'true' and
                          SalesOrder.DocumentState == 'Proceso' and
                          SalesOrder.SalesStatus == 'RED'):
                        DelInventMovements(SalesOrder)
                        SalesOrder.SalesStatus = 'OPE'
                        SalesOrder.DocumentState = 'Abierto'
                        SalesOrder.Enabled = True
                    elif(enabled == 'true' and
                         SalesOrder.DocumentState == 'Cerrado'):
                        SalesOrder.SalesStatus = 'OPE'
                        SalesOrder.DocumentState = 'Abierto'
                        SalesOrder.Enabled = True
                    elif(enabled == 'false' and
                         SalesOrder.DocumentState == 'Cerrado' and
                         SalesOrder.SalesStatus == 'RCA'):
                        DelInventMovements(SalesOrder)
                        SalesOrder.SalesStatus = 'OPE'
                        SalesOrder.DocumentState = 'Abierto'
                        SalesOrder.Enabled = True
                    else:
                        SalesOrder.SalesStatus = 'OPE'
                        SalesOrder.DocumentState = 'Abierto'
                        SalesOrder.Enabled = True
                    SalesOrder.save()

                    response_dict = {
                        'Enabled': SalesOrder.Enabled,
                        'SalesStatus': SalesOrder.SalesStatus,
                        'DocumentState': SalesOrder.DocumentState,
                    }
                return JsonResponse(response_dict)
            elif action == 'reduce_charge':
                if sales_form.is_valid():
                    SalesOrder = sales_form.save(commit=False)
                    SalesOrder.SalesStatus = 'RCA'
                    SalesOrder.Enabled = False
                    SalesOrder.DocumentState = 'Cerrado'
                    SalesOrder.save()

                    for salesline_form in salesline_formset:
                        if salesline_form.is_valid():
                            itemid = salesline_form.cleaned_data.get('ItemId')
                            qty = salesline_form.cleaned_data.get('SalesQty')
                            if itemid and qty:
                                SalesLine = salesline_form.save()
                                SL_list.append(SalesLine.pk)
                                try:
                                    Item = ItemModel.objects.get(ItemId=itemid)
                                    Inventory = InventoryModel.objects.get(
                                        Item=Item,
                                        Location=SalesOrder.Location)
                                    if (Inventory.Qty == 0 or
                                            Inventory.Qty is None):
                                        Inventory.Qty = qty
                                    else:
                                        Inventory.Qty -= qty
                                    Inventory.save()
                                except:
                                    InventoryModel.objects.create(
                                        Item=Item,
                                        Qty=qty,
                                        Location=SalesOrder.Location)
                        else:
                            messages.warning(
                                request,
                                'Revise la información de las lineas de la OV')

                    response_dict = {
                        'Enabled': SalesOrder.Enabled,
                        'SalesStatus': SalesOrder.SalesStatus,
                    }

                    return JsonResponse(response_dict)
                else:
                    salesline_formset = SalesLineFormset(
                        request.POST, prefix='slfs')
                    messages.error(
                        request,
                        "Ocurrió un error al registrar la reducción de inventario")

                return render_to_response(
                    'SalesOrder/UpdateSalesOrder.html',
                    {
                        'sales_form': sales_form,
                        'salesline_formset': salesline_formset,
                        'SalesOrder': SalesOrder
                    },
                    context_instance=RequestContext(request)
                )
            elif action == 'charge_order':
                if sales_form.is_valid():
                    salesStatus = sales_form.cleaned_data.get('SalesStatus')
                    SalesOrder = sales_form.save(commit=False)
                    if salesStatus == 'RED':
                        SalesOrder.SalesStatus = 'RCA'
                        SalesOrder.Enabled = False
                    else:
                        SalesOrder.SalesStatus = 'CAS'
                    SalesOrder.DocumentState = 'Proceso'
                    SalesOrder.save()

                    for salesline_form in salesline_formset:
                        if salesline_form.is_valid():
                            itemid = salesline_form.cleaned_data.get('ItemId')
                            if itemid:
                                SalesLine = salesline_form.save()
                                SL_list.append(SalesLine.pk)
                    response_dict = {
                        'Enabled': SalesOrder.Enabled,
                        'SalesStatus': SalesOrder.SalesStatus,
                    }

                    return JsonResponse(response_dict)
                else:
                    salesline_formset = SalesLineFormset(
                        request.POST, prefix='slfs')
                    messages.error(
                        request, "Ocurrió un error al registrar el cobro")
                    return render_to_response(
                        'SalesOrder/UpdateSalesOrder.html',
                        {'sales_form': sales_form,
                         'salesline_formset': salesline_formset,
                         'SalesOrder': SalesOrder},
                        context_instance=RequestContext(request))
            elif action == 'reduce':
                if sales_form.is_valid():
                    salesStatus = sales_form.cleaned_data.get('SalesStatus')
                    SalesOrder = sales_form.save(commit=False)
                    if salesStatus == 'CAS':
                        SalesOrder.SalesStatus = 'RCA'
                        SalesOrder.Enabled = False
                    else:
                        SalesOrder.SalesStatus = 'RED'
                    SalesOrder.DocumentState = 'Proceso'
                    SalesOrder.save()

                    for salesline_form in salesline_formset:
                        if salesline_form.is_valid():
                            itemid = salesline_form.cleaned_data.get('ItemId')
                            qty = salesline_form.cleaned_data.get('SalesQty')
                            if itemid and qty:
                                SalesLine = salesline_form.save()
                                SL_list.append(SalesLine.pk)
                                try:
                                    Item = ItemModel.objects.get(ItemId=itemid)
                                    Inventory = InventoryModel.objects.get(
                                        Item=Item,
                                        Location=SalesOrder.Location)
                                    if (Inventory.Qty == 0 or
                                            Inventory.Qty is None):
                                        Inventory.Qty = qty
                                    else:
                                        Inventory.Qty -= qty
                                    Inventory.save()
                                    messages.success(
                                        request,
                                        "Artículos reducidos")
                                except:
                                    InventoryModel.objects.create(
                                        Item=Item,
                                        Qty=qty,
                                        Location=SalesOrder.Location)
                        else:
                            messages.warning(
                                request,
                                'Revise la información de las lineas de la OV')
                    response_dict = {
                        'Enabled': SalesOrder.Enabled,
                        'SalesStatus': SalesOrder.SalesStatus,
                    }
                    return JsonResponse(response_dict)
                else:
                    salesline_formset = SalesLineFormset(
                        request.POST, prefix='slfs')
                    messages.error(
                        request,
                        "Ocurrió un error al registrar la reducción de inventario")

                    return render_to_response(
                        'SalesOrder/UpdateSalesOrder.html',
                        {
                            'sales_form': sales_form,
                            'salesline_formset': salesline_formset,
                            'SalesOrder': SalesOrder
                        },
                        context_instance=RequestContext(request)
                    )

            return JsonResponse(response_dict)

        if sales_form.is_valid():
            SO = sales_form.save(commit=False)
            if SO.SalesStatus is not 'RCA' or SO.SalesStatus is not 'INV':
                SO.save()
                messages.success(request, "Orden de venta actualizada")

                for salesline_form in salesline_formset:
                    if salesline_form.is_valid():
                        itemid = salesline_form.cleaned_data.get('ItemId')
                        if itemid:
                            SL = salesline_form.save()
                            SL_list.append(SL.pk)
                    else:
                        messages.warning(
                            request,
                            'Revise la información de las lineas de la OV')
        else:
            salesline_formset = SalesLineFormset(request.POST, prefix='slfs')
            messages.error(
                request, "Ocurrió un error al crear la orden de venta")

        if salesline_formset.is_valid():
            pl = SalesLineModel.objects.filter(SalesOrder=SalesOrder)
            pl.exclude(pk__in=list(SL_list)).delete()

    else:
        sales_form = SalesOrderForm(instance=SalesOrder)
        salesline_formset = SalesLineFormset(
            instance=SalesOrder, prefix='slfs',)

    return render_to_response('SalesOrder/UpdateSalesOrder.html',
                              {'sales_form': sales_form,
                               'salesline_formset': salesline_formset,
                               'SalesOrder': SalesOrder},
                              context_instance=RequestContext(request))


# CBV: View to delete an existing Sales order
# ----------------------------------------------------------------------------
class DeleteSalesOrderView(DeleteView):
    model = SalesOrderModel
    template_name = 'SalesOrder/DeleteSalesOrder.html'
    success_url = '/sales_orders'
    success_message = 'Se ha eliminado la orden de venta'

    def delete(self, request, *args, **kwargs):
        """
        Calls the delete() method on the fetched object and then
        redirects to the success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request,
                         "Se ha eliminado la orden de venta",
                         extra_tags='msg')
        return HttpResponseRedirect(success_url)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


# FBV: Export to csv
@login_required
def export_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response[
        'Content-Disposition'] = 'attachment; filename="ordenes de venta.csv"'

    writer = csv.writer(response)
    writer.writerow(['Órden de venta',
                     'Estado',
                     'Proveedor',
                     'Total',
                     'Cobrado',
                     'Balance', ])
    try:
        orders = SalesOrderModel.objects.all().order_by('created')
        for order in orders:
            writer.writerow([order.SalesId,
                             order.SalesStatus,
                             order.Customer,
                             order.Total,
                             order.Paid,
                             order.Balance, ])
    except:
        return HttpResponseRedirect('/sales_orders/')

    return response


# FBV: Export to pdf
@login_required
def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    # pdf_name = "proveedores.pdf"  # llamado proveedores
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=20,
                            leftMargin=20,
                            topMargin=30,
                            bottomMargin=20,
                            )
    ordenes = []
    styles = getSampleStyleSheet()

    title = Paragraph("Listado de órdenes de venta", styles['Heading2'])
    date = Paragraph(time.strftime("%d/%m/%Y"), styles['Heading2'])
    header = (title, date)
    t = Table([''] + [header] + [''])
    t.setStyle(TableStyle(
        [
            ('ALIGN', (1, 1), (1, 1), 'RIGHT'),
            ('TEXTCOLOR', (0, 1), (0, 0), colors.green),
        ]
    ))
    ordenes.append(t)

    headings = ('Órden de venta', 'Estado', 'Proveedor',
                'Total', 'Cobrado', 'Balance',)
    orders = [(o.SalesId, o.SalesStatus, o.Customer,
               o.Total, o.Paid, o.Balance,)
              for o in SalesOrderModel.objects.all().order_by('created')]

    t = Table([headings] + orders)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (6, -1), 0.5, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 0.5, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    ordenes.append(t)
    doc.build(ordenes)
    response.write(buff.getvalue())
    buff.close()
    return response


# Function: Get Sales Order header data
def GetCustomerInfo(Customer_pk):
    try:
        Customer = CustomerModel.objects.get(pk=Customer_pk)
    except:
        Customer = None
    NameAlias = (
        Customer.Party.NameAlias if Customer.Party.NameAlias else '')
    VATNum = (Customer.VATNum if Customer.VATNum else '')
    CurrencyCode = (
        Customer.CurrencyCode if Customer.CurrencyCode else '')
    LanguageCode = (
        (Customer.Party.LanguageCode)
        if Customer.Party.LanguageCode else '')
    OneTimeCustomer = (
        Customer.OneTimeCustomer if Customer.OneTimeCustomer else '')
    DeliveryName = Customer.get_PrimaryAddress(
    ) if Customer.get_PrimaryAddress() else ''
    DeliveryContact = Customer.get_PrimaryElectronic(
    ) if Customer.get_PrimaryElectronic() else ''
    response_dict = {
        'NameAlias': NameAlias,
        'VATNum': VATNum,
        'CurrencyCode': CurrencyCode,
        'LanguageCode': LanguageCode,
        'OneTimeCustomer': OneTimeCustomer,
        'DeliveryName': DeliveryName,
        'DeliveryContact': DeliveryContact,
    }
    return response_dict


# Function: Get Sales Order header data
def GetLineInfo(Item_pk):
    # Get item object
    try:
        Item = ItemModel.objects.get(pk=Item_pk)
        ItemName = Item.ItemName
        SalesPrice = Item.Price
    except:
        ItemName = ''
    # Get EcoResProduct object
    try:
        EcoResProduct = EcoResProductModel.objects.get(Item=Item)
        SalesUnit = EcoResProduct.SalesUnit
    except:
        SalesUnit = ''
    # Get item object
    response_dict = {
        'ItemName': ItemName,
        'UnitId': SalesUnit,
        'SalesPrice': SalesPrice,
    }
    return response_dict


# Function: Get Sales Order header data
def DelInventMovements(SalesOrder):
    SalesLines = SalesLineModel.objects.filter(SalesOrder=SalesOrder)
    for SalesLine in SalesLines:
        try:
            InventoryItem = InventoryModel.objects.get(
                Q(Item=SalesLine.ItemId) & Q(Location=SalesOrder.Location))
            InventoryItem.Qty += SalesLine.SalesQty
            InventoryItem.save()
        except:
            InventoryItem = None

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-14 15:29:39
# @Last Modified by:   Alex
# @Last Modified time: 2016-01-02 17:33:18
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Count, Sum
from Inventationery.apps.Company.models import CompanyInfoModel
from Inventationery.apps.PurchOrder.models import (
    PurchOrderModel, PurchLineModel)
from Inventationery.apps.SalesOrder.models import (
    SalesOrderModel, SalesLineModel)
from Inventationery.apps.Inventory.models import (ItemModel, InventoryModel)
# Create your views here.


@login_required
def Home(request):
    # Company Model
    try:
        Company = CompanyInfoModel.objects.all()[:1]
    except:
        Company = []

    # Get PurchOrder
    try:
        PurchOrders = PurchOrderModel.objects.all()
    except:
        PurchOrders = []

    # Get SalesOrder
    try:
        SalesOrders = SalesOrderModel.objects.all()
    except:
        SalesOrders = []

    # Get SalesOrder
    try:
        SalesOrders = SalesOrderModel.objects.all()
    except:
        SalesOrders = []

    # Get ItemsSold
    try:
        ItemsSold = SalesLineModel.objects.aggregate(Vendidos=Sum('SalesQty'))
    except:
        ItemsSold = []

    # Get ItemsPurchased
    try:
        ItemsPurchased = PurchLineModel.objects.aggregate(
            Comprados=Sum('PurchQty'))
    except:
        ItemsPurchased = []
    # Get ItemModel
    try:
        Items = ItemModel.objects.all()
    except:
        Items = []

    if request.method == 'POST' and request.is_ajax():
        action = request.POST.get('action', '')
        if action == 'today':
            GetMonthlyStats()
        if action == 'this_week':
            GetMonthlyStats()
        if action == 'this_month':
            GetMonthlyStats()
        if action == 'this_year':
            GetMonthlyStats()
        if action == 'yesterday':
            GetMonthlyStats()
        if action == 'last_week':
            GetMonthlyStats()
        if action == 'last_month':
            GetMonthlyStats()
        if action == 'last_year':
            GetMonthlyStats()
        if action == 'last_7_days':
            GetMonthlyStats()
        if action == 'last_30_days':
            GetMonthlyStats()
        if action == 'last_365_days':
            GetMonthlyStats()
        if action == 'last_year':
            GetMonthlyStats()

    return render_to_response('home/home.html',
                              {'Company': Company,
                               'PurchOrders': PurchOrders,
                               'SalesOrders': SalesOrders,
                               'Purch_open': GetOpenPurchOrders(),
                               'Purch_process': GetProcessPurchOrders(),
                               'Purch_closed': GetClosedPurchOrders(),
                               'Sales_open': GetOpenSalesOrders(),
                               'Sales_process': GetProcessSalesOrders(),
                               'Sales_closed': GetClosedSalesOrders(),
                               'ItemsSold': ItemsSold,
                               'ItemsPurchased': ItemsPurchased,
                               'Items': Items,
                               'PurchTotal': GetPurchTotals,
                               'SalesTotal': GetSalesTotals, },
                              context_instance=RequestContext(request))


def GetOpenPurchOrders():
    try:
        Open = PurchOrderModel.objects.filter(DocumentState='Abierto').count()
    except:
        Open = ''

    return Open


def GetProcessPurchOrders():
    try:
        Process = PurchOrderModel.objects.filter(
            DocumentState='Proceso').count()
    except:
        Process = ''

    return Process


def GetClosedPurchOrders():
    try:
        Closed = PurchOrderModel.objects.filter(
            DocumentState='Cerrado').count()
    except:
        Closed = ''

    return Closed


def GetOpenSalesOrders():
    try:
        Open = SalesOrderModel.objects.filter(DocumentState='Abierto').count()
    except:
        Open = ''

    return Open


def GetProcessSalesOrders():
    try:
        Process = SalesOrderModel.objects.filter(
            DocumentState='Proceso').count()
    except:
        Process = ''

    return Process


def GetClosedSalesOrders():
    try:
        Closed = SalesOrderModel.objects.filter(
            DocumentState='Cerrado').count()
    except:
        Closed = ''

    return Closed


def GetPurchTotals():
    Total = 0
    try:
        PurchOrders = PurchOrderModel.objects.all()
        for order in PurchOrders:
            Total += order.Total
    except:
        Total = 0

    return Total


def GetSalesTotals():
    Total = 0
    try:
        SalesOrders = SalesOrderModel.objects.all()
        for order in SalesOrders:
            Total += order.Total
    except:
        Total = 0

    return Total

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:10:36
# @Last Modified by:   Alex
# @Last Modified time: 2016-01-02 14:43:41
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.db.models import Q, Count
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.forms import inlineformset_factory
from django.views.generic import (ListView, DeleteView, CreateView, UpdateView)
import csv
import time
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from .models import (ItemModel, InventoryModel,
                     ItemVendorModel, EcoResProductModel,
                     MovementHistoryModel, OrderHistoryModel, LocationModel)
from .forms import (InventoryForm, ItemForm, ItemVendorForm,
                    EcoResProductForm, LocationForm)


# CBV: View to list all inventory items
# ----------------------------------------------------------------------------
class InventListView(ListView):
    model = ItemModel
    form_class = ItemForm
    template_name = 'Inventory/InventoryList.html'
    context_object_name = 'items'

    def get_queryset(self):
        queryset = super(InventListView, self).get_queryset()
        queryset = ItemModel.objects.all().order_by('ItemId')
        return queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


# CBV: View to list all items in existance
# ----------------------------------------------------------------------------
class InventExistingListView(ListView):
    model = ItemModel
    form_class = ItemForm
    template_name = 'Inventory/InventoryList.html'
    context_object_name = 'items'

    def get_queryset(self):
        queryset = super(InventExistingListView, self).get_queryset()
        queryset = ItemModel.objects.filter(
            Item__isnull=False).annotate(Count('Item'))
        # queryset = ItemModel.objects.all().order_by('ItemId')
        return queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


# FBV: View to create a new Item on inventory
@login_required
def createInventView(request):
    InventoryFormset = inlineformset_factory(
        ItemModel,
        InventoryModel,
        extra=1,
        fields='__all__',
        form=InventoryForm)
    ItemVendorFormset = inlineformset_factory(
        ItemModel,
        ItemVendorModel,
        extra=1,
        fields='__all__',
        form=ItemVendorForm)
    IN_list = []
    IV_list = []
    if request.method == 'POST':
        item_form = ItemForm(request.POST, request.FILES)
        ecoResProductForm = EcoResProductForm(request.POST)
        if item_form.is_valid():
            image = request.FILES.get('ItemImage')
            item = item_form.save()
            inventory_formset = InventoryFormset(
                request.POST, instance=item, prefix='infs')
            itemVendor_formset = ItemVendorFormset(
                request.POST, instance=item, prefix='ivfs')
        else:
            inventory_formset = InventoryFormset(prefix='infs')
            itemVendor_formset = ItemVendorFormset(prefix='ivfs')
            messages.error(request, 'Revise la información del artículo')

        if ecoResProductForm.is_valid():
            ecoResProduct = ecoResProductForm.save(commit=False)
            ecoResProduct.Item = item
            ecoResProduct.save()
        else:
            messages.error(
                request, 'Revise la información adicional del artículo')

        if inventory_formset.is_valid():
            for invent_form in inventory_formset:
                if invent_form.is_valid():
                    qty = invent_form.cleaned_data.get('Qty')
                    location = invent_form.cleaned_data.get('Location')
                    if qty and location:
                        invent = invent_form.save(commit=False)
                        invent.Item = item
                        invent.save()
                        # Set movement history
                        SetMovementHistory(
                            item, 'ADJUSTMENT', invent.created,
                            invent.Location, '',
                            invent.Qty, 0, invent.Qty, request.user)
                        IN_list.append(invent.pk)
            inl = InventoryModel.objects.filter(Item=item)
            inl.exclude(pk__in=list(IN_list)).delete()
        if itemVendor_formset.is_valid():
            for itemVendorForm in itemVendor_formset:
                if itemVendorForm.is_valid():
                    vendorPrice = itemVendorForm.cleaned_data.get(
                        'VendorPrice')
                    vendor = itemVendorForm.cleaned_data.get('Vendor')
                    if vendor and vendorPrice:
                        itemVendor = itemVendorForm.save(commit=False)
                        itemVendor.Item = item
                        itemVendor.save()
                        IV_list.append(itemVendor.pk)
            ivl = ItemVendorModel.objects.filter(Item=item)
            ivl.exclude(pk__in=list(IV_list)).delete()
        else:
            messages.error(request, 'Revise la información de inventario')

        if item_form.is_valid() and inventory_formset.is_valid():
            messages.success(
                request, 'Artículo creado correctamente \
                y asignado al inventario')

            redirect_url = "/Item/update/" + str(item.ItemId)
            return HttpResponseRedirect(redirect_url)
    else:
        item_form = ItemForm()
        itemVendor_formset = ItemVendorFormset(prefix='ivfs')
        ecoResProductForm = EcoResProductForm()
        inventory_formset = InventoryFormset(prefix='infs')

    return render_to_response('Inventory/CreateInvent.html',
                              {'item_form': item_form,
                               'itemVendor_formset': itemVendor_formset,
                               'ecoResProductForm': ecoResProductForm,
                               'inventory_formset': inventory_formset},
                              context_instance=RequestContext(request))


# FBV: View to update a new Item on inventory
@login_required
def updateInventView(request, ItemId):
    Item = get_object_or_404(ItemModel, ItemId=ItemId)
    try:
        ecoResProduct = EcoResProductModel.objects.get(Item=Item)
    except:
        ecoResProduct = None
    IN_list = []
    IV_list = []
    InventoryFormset = inlineformset_factory(
        ItemModel,
        InventoryModel,
        extra=1,
        fields='__all__',
        form=InventoryForm)
    ItemVendorFormset = inlineformset_factory(
        ItemModel,
        ItemVendorModel,
        extra=1,
        fields='__all__',
        form=ItemVendorForm)
    if request.method == 'POST':
        item_form = ItemForm(request.POST, request.FILES, instance=Item)
        ecoResProductForm = EcoResProductForm(
            request.POST, instance=ecoResProduct)
        inventory_formset = InventoryFormset(
            request.POST, instance=Item, prefix='infs')
        itemVendor_formset = ItemVendorFormset(
            request.POST, instance=Item, prefix='ivfs')

        if item_form.is_valid():
            image = request.FILES.get('ItemImage')
            item = item_form.save()
            print request.FILES
        else:
            messages.error(request, 'Revise la información del artículo')

        if ecoResProductForm.is_valid():
            ecoResProduct = ecoResProductForm.save(commit=False)
            ecoResProduct.Item = Item
            ecoResProduct.save()
        else:
            messages.error(
                request, 'Revise la información adicional del artículo')

        if inventory_formset.is_valid():
            for invent_form in inventory_formset:
                if invent_form.is_valid():
                    qty = invent_form.cleaned_data.get('Qty')
                    location = invent_form.cleaned_data.get('Location')
                    if qty and location:
                        try:
                            inventPrev = InventoryModel.objects.filter(
                                Q(Location=location) & Q(Item=item)).get()
                            prev_qty = inventPrev.Qty
                        except:
                            prev_qty = 0
                        invent = invent_form.save(commit=False)
                        invent.Item = item
                        invent.save()
                        IN_list.append(invent.pk)
                        if qty != prev_qty:
                            # Set movement history
                            SetMovementHistory(
                                item, 'ADJUSTMENT', invent.created,
                                invent.Location, '',
                                invent.Qty, prev_qty,
                                invent.Qty, request.user)
            inl = InventoryModel.objects.filter(Item=item)
            inl.exclude(pk__in=list(IN_list)).delete()
        else:
            messages.error(request, 'Revise la información de inventario')

        if itemVendor_formset.is_valid():
            for itemVendorForm in itemVendor_formset:
                if itemVendorForm.is_valid():
                    vendorPrice = itemVendorForm.cleaned_data.get(
                        'VendorPrice')
                    vendor = itemVendorForm.cleaned_data.get('Vendor')
                    if vendor and vendorPrice:
                        itemVendor = itemVendorForm.save(commit=False)
                        itemVendor.Item = item
                        itemVendor.save()
                        IV_list.append(itemVendor.pk)
            ivl = ItemVendorModel.objects.filter(Item=Item)
            ivl.exclude(pk__in=list(IV_list)).delete()
        else:
            messages.error(
                request, 'Revise la información del proveedor de artículos')

        if (item_form.is_valid() and
                inventory_formset.is_valid() and
                itemVendor_formset.is_valid()):
            messages.success(
                request, 'Artículo actualizado correctamente \
                y asignado al inventario')
        else:
            messages.error(
                request, "Ocurrió un error al actualizar el artículo",
                extra_tags='msg')
    else:
        item_form = ItemForm(instance=Item)
        itemVendor_formset = ItemVendorFormset(prefix='ivfs', instance=Item)
        ecoResProductForm = EcoResProductForm(instance=ecoResProduct)
        inventory_formset = InventoryFormset(prefix='infs', instance=Item)

    try:
        movement_history = MovementHistoryModel.objects.filter(Item=Item)
    except:
        movement_history = []
    try:
        order_history = OrderHistoryModel.objects.filter(Item=Item)
    except:
        order_history = []
    return render_to_response('Inventory/UpdateInvent.html',
                              {'Item': Item,
                               'item_form': item_form,
                               'itemVendor_formset': itemVendor_formset,
                               'ecoResProductForm': ecoResProductForm,
                               'movement_history': movement_history,
                               'order_history': order_history,
                               'inventory_formset': inventory_formset},
                              context_instance=RequestContext(request))


# CBV: View to delete an existing Item on inventory
# ----------------------------------------------------------------------------
class DeleteInventView(DeleteView):
    model = ItemModel
    form_class = ItemForm
    template_name = 'Inventory/DeleteInvent.html'
    success_url = '/Item'
    slug_field = 'ItemId'
    slug_url_kwarg = 'ItemId'

    def delete(self, request, *args, **kwargs):
        """
        Calls the delete() method on the fetched object and then
        redirects to the success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request,
                         "Artículo eliminado correctamente",
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
    response['Content-Disposition'] = 'attachment; filename="artículos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Código',
                     'Nombre',
                     'Descripción',
                     'Unidad venta',
                     'Precio venta',
                     'Proveedor principal',
                     'Precio compra'])
    try:
        item_list = ItemModel.objects.all().order_by('ItemId')
        for item in item_list:
            ecoRes = EcoResProductModel.objects.filter(Item=item)
            itemVend = ItemVendorModel.objects.filter(
                Item=item, Vendor=item.PrimaryVendor)
            writer.writerow([item.ItemId,
                             item.ItemName,
                             item.Description,
                             ecoRes.SalesUnit,
                             item.Price,
                             item.PrimaryVendor,
                             itemVend.VendorPrice])
    except:
        return HttpResponseRedirect('/Item/')

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
    articulos = []
    styles = getSampleStyleSheet()

    title = Paragraph("Listado de artículos", styles['Heading2'])
    date = Paragraph(time.strftime("%d/%m/%Y"), styles['Heading2'])
    header = (title, date)
    t = Table([''] + [header] + [''])
    t.setStyle(TableStyle(
        [
            ('ALIGN', (1, 1), (1, 1), 'RIGHT'),
            ('TEXTCOLOR', (0, 1), (0, 0), colors.green),
        ]
    ))
    articulos.append(t)

    headings = ('Código', 'Nombre', 'Descripción',
                'Unidad', 'Precio venta', 'Proveedor principal',
                'Precio compra')
    items = [(i.ItemId, i.ItemName, i.Description,
              i.Price, i.Price, i.PrimaryVendor,
              i.VendorPrice)
             for i in ItemModel.objects.all().order_by('ItemId')]

    t = Table([headings] + items)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (6, -1), 0.5, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 0.5, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    articulos.append(t)
    doc.build(articulos)
    response.write(buff.getvalue())
    buff.close()
    return response


# Set history record for ADJUSTMENT movement
def SetMovementHistory(_Item,
                       _TransactionType,
                       _Date,
                       _Location,
                       _Document,
                       _qty,
                       _qty_p,
                       _qty_a,
                       _user):
    MovementHistoryModel.objects.create(Item=_Item,
                                        TransactionType=_TransactionType,
                                        Date=_Date,
                                        Location=_Location,
                                        Notes=_Document,
                                        Qty=_qty,
                                        Qty_prev=_qty_p,
                                        Qty_after=_qty_a,
                                        user=_user)


# CBV: View to list locations for inventory
# ----------------------------------------------------------------------------
class ListLocationView(ListView):
    model = LocationModel
    form_class = LocationForm
    template_name = 'Inventory/LocationList.html'
    context_object_name = 'locations'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


# CBV: View to create a location for inventory
# ----------------------------------------------------------------------------
class CreateLocationView(CreateView):
    model = LocationModel
    form_class = LocationForm
    template_name = 'Inventory/CreateLocation.html'
    success_url = '/Location/'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


# CBV: View to update a location for inventory
# ----------------------------------------------------------------------------
class UpdateLocationView(UpdateView):
    model = LocationModel
    form_class = LocationForm
    template_name = 'Inventory/UpdateLocation.html'
    slug_url_kwarg = 'LocationName'
    slug_field = 'LocationName'
    context_object_name = 'Location'
    success_url = '/Location/'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


# CBV: View to delete a location for inventory
# ----------------------------------------------------------------------------
class DeleteLocationView(DeleteView):
    model = LocationModel
    form_class = LocationForm
    template_name = 'Inventory/DeleteLocation.html'
    slug_url_kwarg = 'LocationName'
    slug_field = 'LocationName'
    context_object_name = 'Location'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

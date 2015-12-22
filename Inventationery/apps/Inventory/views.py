#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:10:36
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-21 22:01:25
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.forms import inlineformset_factory
from django.views.generic import (ListView, DeleteView)
import csv
import time
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from .models import ItemModel, InventoryModel
from .forms import InventoryForm, ItemForm


# FBV: View to create a new Item on inventory
def createInventView(request):
    InventoryFormset = inlineformset_factory(
        ItemModel,
        InventoryModel,
        extra=1,
        fields='__all__',
        form=InventoryForm)
    if request.method == 'POST':
        item_form = ItemForm(request.POST)

        if item_form.is_valid():
            item = item_form.save()
            inventory_formset = InventoryFormset(
                request.POST, instance=item, prefix='infs')
        else:
            inventory_formset = InventoryFormset(
                request.POST, prefix='infs')
            messages.error(request, 'Revise la información del artículo')

        if inventory_formset.is_valid():
            for invent_form in inventory_formset:
                if invent_form.is_valid():
                    qty = invent_form.cleaned_data.get('Qty')
                    location = invent_form.cleaned_data.get('Location')
                    if qty and location:
                        invent = invent_form.save(commit=False)
                        invent.Item = item
                        invent.save()
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
        inventory_formset = InventoryFormset(prefix='infs')

    return render_to_response('Inventory/CreateInvent.html',
                              {'item_form': item_form,
                               'inventory_formset': inventory_formset},
                              context_instance=RequestContext(request))


# FBV: View to update a new Item on inventory
def updateInventView(request, ItemId):
    Item = get_object_or_404(ItemModel, ItemId=ItemId)
    IN_list = []
    InventoryFormset = inlineformset_factory(
        ItemModel,
        InventoryModel,
        extra=1,
        fields='__all__',
        form=InventoryForm)
    if request.method == 'POST':
        item_form = ItemForm(request.POST, instance=Item)
        inventory_formset = InventoryFormset(
            request.POST, instance=Item, prefix='infs')

        if item_form.is_valid():
            item = item_form.save()
        else:
            messages.error(request, 'Revise la información del artículo')

        if inventory_formset.is_valid():
            for invent_form in inventory_formset:
                if invent_form.is_valid():
                    qty = invent_form.cleaned_data.get('Qty')
                    location = invent_form.cleaned_data.get('Location')
                    if qty and location:
                        invent = invent_form.save(commit=False)
                        invent.Item = item
                        invent.save()
                        IN_list.append(invent.pk)
            InventoryModel.objects.exclude(
                pk__in=list(IN_list)).delete()
        else:
            messages.error(request, 'Revise la información de inventario')

        if item_form.is_valid() and inventory_formset.is_valid():
            messages.success(
                request, 'Artículo actualizado correctamente \
                y asignado al inventario')
        else:
            messages.error(
                request, "Ocurrió un error al actualizar el artículo",
                extra_tags='msg')
    else:
        item_form = ItemForm(instance=Item)
        inventory_formset = InventoryFormset(prefix='infs', instance=Item)

    return render_to_response('Inventory/UpdateInvent.html',
                              {'item_form': item_form,
                               'inventory_formset': inventory_formset},
                              context_instance=RequestContext(request))


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


# CBV: View to delete an existing Item on inventory
# ----------------------------------------------------------------------------
class DeleteInventView(DeleteView):
    model = ItemModel
    form_class = ItemForm
    template_name = 'Inventory/DeleteInvent.html'
    success_url = '/Item'

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


# FBV: Export to csv
# ----------------------------------------------------------------------------
def export_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="artículos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Código',
                     'Nombre',
                     'Descripción',
                     'Unidad',
                     'Precio venta',
                     'Proveedor principal',
                     'Precio compra'])
    try:
        item_list = ItemModel.objects.all().order_by('ItemId')
        for item in item_list:
            writer.writerow([item.ItemId,
                             item.ItemName,
                             item.Description,
                             item.UnitId,
                             item.Price,
                             item.PrimaryVendor,
                             item.VendorPrice])
    except:
        return HttpResponseRedirect('/Item/')

    return response


# FBV: Export to pdf
# ----------------------------------------------------------------------------
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
              i.UnitId, i.Price, i.PrimaryVendor,
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

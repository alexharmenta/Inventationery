#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:10:36
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-06 17:28:57
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.forms import inlineformset_factory
from django.views.generic import (ListView, DeleteView)
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

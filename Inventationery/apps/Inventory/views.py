#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:10:36
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-30 21:23:04
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import (CreateView,
                                  ListView,
                                  UpdateView,
                                  DeleteView)
from .models import ItemModel
from .forms import InventForm


# CBV: View to create a new Item on inventory
# ----------------------------------------------------------------------------
class CreateInventView(CreateView):
    model = ItemModel
    form_class = InventForm
    template_name = 'Inventory/CreateInvent.html'
    success_url = '/Item'

    def form_valid(self, form):
        messages.success(
            self.request, "Artículo creado correctamente", extra_tags='msg')
        return super(CreateInventView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Ocurrió un error al registrar el artículo",
            extra_tags='msg')
        return super(CreateInventView, self).form_valid(form)


# CBV: View to list all inventory items
# ----------------------------------------------------------------------------
class InventListView(ListView):
    model = ItemModel
    form_class = InventForm
    template_name = 'Inventory/InventoryList.html'
    context_object_name = 'items'

    def get_queryset(self):
        queryset = super(InventListView, self).get_queryset()
        queryset = ItemModel.objects.all().order_by('ItemId')
        return queryset


# CBV: View to update an existing Item on inventory
# ----------------------------------------------------------------------------
class UpdateInventView(UpdateView):
    model = ItemModel
    form_class = InventForm
    template_name = 'Inventory/UpdateInvent.html'

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        messages.success(self.request,
                         "Artículo actualizado correctamente",
                         extra_tags='msg')
        return super(UpdateInventView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            "Ocurrió un error al actualizar el artículo",
            extra_tags='msg')
        return super(UpdateInventView, self).form_valid(form)


# CBV: View to delete an existing Item on inventory
# ----------------------------------------------------------------------------
class DeleteInventView(DeleteView):
    model = ItemModel
    form_class = InventForm
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

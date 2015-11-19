#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:10:36
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-18 21:19:20
from django.views.generic import (CreateView,
                                  ListView,
                                  UpdateView,
                                  DeleteView)
from .models import InventModel
from .forms import InventForm


# CBV: View to create a new Item on inventory
# ----------------------------------------------------------------------------
class CreateInventView(CreateView):
    model = InventModel
    form_class = InventForm
    template_name = 'Inventory/CreateInvent.html'
    success_url = '/Item'


# CBV: View to list all inventory items
# ----------------------------------------------------------------------------
class InventListView(ListView):
    model = InventModel
    form_class = InventForm
    template_name = 'Inventory/InventoryList.html'
    context_object_name = 'items'

    def get_queryset(self):
        queryset = super(InventListView, self).get_queryset()
        queryset = InventModel.objects.all().order_by('ItemId')
        return queryset


# CBV: View to update an existing Item on inventory
# ----------------------------------------------------------------------------
class UpdateInventView(UpdateView):
    model = InventModel
    form_class = InventForm
    template_name = 'Inventory/UpdateInvent.html'

    def get_success_url(self):
        return self.request.path


# CBV: View to delete an existing Item on inventory
# ----------------------------------------------------------------------------
class DeleteInventView(DeleteView):
    model = InventModel
    form_class = InventForm
    template_name = 'Inventory/DeleteInvent.html'
    success_url = '/Item'

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:10:36
# @Last Modified by:   Alex
# @Last Modified time: 2015-11-16 19:25:23
from django.views.generic import (CreateView,
                                  ListView,
                                  UpdateView,
                                  DeleteView)
from .models import InventModel
from .forms import InventForm

# Create your views here.


class CreateInventView(CreateView):
    model = InventModel
    form_class = InventForm
    template_name = 'Invent/CreateInvent.html'
    success_url = '/Items'


class InventListView(ListView):
    model = InventModel
    form_class = InventForm
    template_name = 'Invent/InventoryList.html'
    context_object_name = 'items'

    def get_queryset(self):
        queryset = super(InventListView, self).get_queryset()
        queryset = InventModel.objects.all().order_by('ItemId')
        return queryset


class UpdateInventView(UpdateView):
    model = InventModel
    form_class = InventForm
    template_name = 'Invent/UpdateInvent.html'

    def get_success_url(self):
        return self.request.path


class DeleteInventView(DeleteView):
    model = InventModel
    form_class = InventForm
    template_name = 'Invent/DeleteInvent.html'
    success_url = '/Items'

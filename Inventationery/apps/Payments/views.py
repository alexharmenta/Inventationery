#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-12-20 22:05:42
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-29 00:03:05
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, CreateView, UpdateView
from .models import PaymentModel, PaymModeModel
from .forms import PaymentForm, PaymModeForm


# CBV: View to add a new Payment
# ----------------------------------------------------------------------------
class CreatePaymentView(CreateView):
    model = PaymentModel
    template_name = 'Payment/CreatePayment.html'
    success_url = '/purch_orders'
    success_message = 'Condición de pago creada correctamente'
    form_class = PaymentForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


# CBV: View to update an existing Payment
# ----------------------------------------------------------------------------
class UpdatePaymentView(UpdateView):
    model = PaymentModel
    template_name = 'Payment/UpdatePayment.html'
    success_url = '/purch_orders'
    success_message = 'Condición de pago actualizada correctamente'
    form_class = PaymentForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


# CBV: View to delete an existing Payment
# ----------------------------------------------------------------------------
class DeletePaymentView(DeleteView):
    model = PaymentModel
    template_name = 'Payment/DeletePayment.html'
    success_url = '/purch_orders'
    success_message = 'Condición de pago eliminada correctamente'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


# CBV: View to add a new Payment
# ----------------------------------------------------------------------------
class CreatePaymModeView(CreateView):
    model = PaymModeModel
    template_name = 'Payment/CreatePaymMode.html'
    success_url = '/purch_orders'
    success_message = 'Modo de pago creada correctamente'
    form_class = PaymModeForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


# CBV: View to update an existing Payment
# ----------------------------------------------------------------------------
class UpdatePaymModeView(UpdateView):
    model = PaymModeModel
    template_name = 'Payment/UpdatePaymMode.html'
    success_url = '/purch_orders'
    success_message = 'Modo de pago actualizada correctamente'
    form_class = PaymModeForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


# CBV: View to delete an existing Payment
# ----------------------------------------------------------------------------
class DeletePaymModeView(DeleteView):
    model = PaymModeModel
    template_name = 'Payment/DeletePaymMode.html'
    success_url = '/purch_orders'
    success_message = 'Modo de pago eliminada correctamente'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)

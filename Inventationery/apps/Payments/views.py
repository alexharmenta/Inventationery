#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-12-20 22:05:42
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-20 22:25:50
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


# CBV: View to update an existing Payment
# ----------------------------------------------------------------------------
class UpdatePaymentView(UpdateView):
    model = PaymentModel
    template_name = 'Payment/UpdatePayment.html'
    success_url = '/purch_orders'
    success_message = 'Condición de pago actualizada correctamente'
    form_class = PaymentForm


# CBV: View to delete an existing Payment
# ----------------------------------------------------------------------------
class DeletePaymentView(DeleteView):
    model = PaymentModel
    template_name = 'Payment/DeletePayment.html'
    success_url = '/purch_orders'
    success_message = 'Condición de pago eliminada correctamente'


# CBV: View to add a new Payment
# ----------------------------------------------------------------------------
class CreatePaymModeView(CreateView):
    model = PaymModeModel
    template_name = 'Payment/CreatePaymMode.html'
    success_url = '/purch_orders'
    success_message = 'Modo de pago creada correctamente'
    form_class = PaymModeForm


# CBV: View to update an existing Payment
# ----------------------------------------------------------------------------
class UpdatePaymModeView(UpdateView):
    model = PaymModeModel
    template_name = 'Payment/UpdatePaymMode.html'
    success_url = '/purch_orders'
    success_message = 'Modo de pago actualizada correctamente'
    form_class = PaymModeForm


# CBV: View to delete an existing Payment
# ----------------------------------------------------------------------------
class DeletePaymModeView(DeleteView):
    model = PaymModeModel
    template_name = 'Payment/DeletePaymMode.html'
    success_url = '/purch_orders'
    success_message = 'Modo de pago eliminada correctamente'

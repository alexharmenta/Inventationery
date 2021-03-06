#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-12-20 22:05:42
# @Last Modified by:   Alex
# @Last Modified time: 2016-01-02 20:01:50
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, CreateView, UpdateView
from django.forms import formset_factory
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


# FBV: View for manage payments
@login_required
@permission_required('is_staff')
def PaymentsView(request):
    P_list = []
    PM_list = []
    try:
        Payments = list(PaymentModel.objects.all().values())
    except:
        Payments = []

    try:
        PaymModes = list(PaymModeModel.objects.all().values())
    except:
        PaymModes = []

    PaymentsFormset = formset_factory(
        PaymentForm, extra=1)
    PaymModesFormset = formset_factory(
        PaymModeForm, extra=1)

    if request.method == 'POST':
        payments_formset = PaymentsFormset(request.POST, prefix='pfs')
        paymmodes_formset = PaymModesFormset(request.POST, prefix='pmfs')

        for payment_form in payments_formset:
            if payment_form.is_valid():
                paymCode = payment_form.cleaned_data.get('PaymCode')
                if paymCode:
                    payment = payment_form.save()
                    P_list.append(payment.pk)
        pl = PaymentModel.objects.all()
        pl.exclude(pk__in=list(P_list)).delete()
        for paymmode_form in paymmodes_formset:
            if paymmode_form.is_valid():
                paymModeCode = paymmode_form.cleaned_data.get('PaymModeCode')
                if paymModeCode:
                    paymmode = paymmode_form.save()
                    PM_list.append(paymmode.pk)
        pml = PaymModeModel.objects.all()
        pml.exclude(pk__in=list(PM_list)).delete()
        messages.success(
            request, 'Pagos creados correctamente')
    else:
        payments_formset = PaymentsFormset(initial=Payments, prefix='pfs')
        paymmodes_formset = PaymModesFormset(initial=PaymModes, prefix='pmfs')

    return render_to_response('Payment/ManagePayments.html',
                              {'payments_formset': payments_formset,
                               'paymmodes_formset': paymmodes_formset, },
                              context_instance=RequestContext(request))

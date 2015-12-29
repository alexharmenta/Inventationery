#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 19:22:12
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-28 23:55:35
# views.py
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.views.generic import ListView, DeleteView
import csv
import time
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.lib.pagesizes import landscape
from .models import CustomerModel
from Inventationery.apps.DirParty.models import DirPartyModel
from Inventationery.apps.LogisticsPostalAddress.models import (
    LogisticsPostalAddressModel)
from Inventationery.apps.LogisticsElectronicAddress.models import (
    LogisticsElectronicAddressModel)
from .forms import (CustomerForm,
                    PartyForm,)


# CBV: View to list all customers ordered by AccountNum
# ----------------------------------------------------------------------------
class CustomerListView(ListView):
    model = CustomerModel
    template_name = 'customer/CustomerList.html'
    context_object_name = 'customers'

    def get_queryset(self):
        queryset = super(CustomerListView, self).get_queryset()
        queryset = CustomerModel.objects.all().order_by('AccountNum')
        return queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


# FBV: View for create new Customer
@login_required
def createCustomerView(request):

    customer = CustomerModel()
    party = DirPartyModel()

    ElectronicFormSet = inlineformset_factory(
        DirPartyModel, LogisticsElectronicAddressModel,
        extra=1, max_num=5, fields='__all__')
    PostalFormSet = inlineformset_factory(
        DirPartyModel, LogisticsPostalAddressModel,
        extra=1, max_num=5, fields='__all__')

    if request.method == 'POST':
        # formulario enviado
        customer_form = CustomerForm(request.POST)
        party_form = PartyForm(request.POST)

        electronic_formset = ElectronicFormSet(
            request.POST, instance=party, prefix='efs')
        postal_formset = PostalFormSet(
            request.POST, instance=party, prefix='pfs')

        if customer_form.is_valid() and party_form.is_valid():

            electronic_formset = ElectronicFormSet(
                request.POST, instance=party, prefix='efs')
            postal_formset = PostalFormSet(
                request.POST, instance=party, prefix='pfs')

            party = party_form.save()
            customer = customer_form.save(commit=False)
            customer.Party = party
            customer.save()
            messages.success(request, "Proveedor creado correctamente")

            for electronic_form in electronic_formset:
                if electronic_form.is_valid():
                    description = electronic_form.cleaned_data.get(
                        'Description')
                    contact = electronic_form.cleaned_data.get('Contact')
                    if description and contact:
                        Electronic = electronic_form.save(commit=False)
                        Electronic.Party = party
                        Electronic.save()
                else:
                    messages.warning(
                        request, 'Revise la información de contacto')

            for postal_form in postal_formset:
                if postal_form.is_valid():
                    description = postal_form.cleaned_data.get(
                        'Description')
                    if description:
                        Postal = postal_form.save(commit=False)
                        Postal.Party = party
                        Postal.save()
                else:
                    messages.warning(
                        request, 'Revise la información de la dirección')

            redirect_url = "/customer/update/" + str(customer.AccountNum)
            return HttpResponseRedirect(redirect_url)
        else:
            messages.error(
                request, "Ocurrió un error al crear el proveedor")

    else:
        # formulario inicial
        customer_form = CustomerForm(instance=customer)
        party_form = PartyForm(instance=party)
        electronic_formset = ElectronicFormSet(
            prefix='efs', instance=party)
        postal_formset = PostalFormSet(prefix='pfs', instance=party)

    return render_to_response('customer/CreateCustomer.html',
                              {'customer_form': customer_form,
                               'party_form': party_form,
                               'electronic_formset': electronic_formset,
                               'postal_formset': postal_formset, },
                              context_instance=RequestContext(request))


# FBV: View for update an existing Customer
@login_required
def updateCustomerView(request, AccountNum):
    Customer = get_object_or_404(CustomerModel, AccountNum=AccountNum)
    Party = Customer.Party
    EA_list = []
    PA_list = []

    ElectronicFormSet = inlineformset_factory(
        DirPartyModel, LogisticsElectronicAddressModel,
        extra=1, max_num=5, fields='__all__')
    PostalFormSet = inlineformset_factory(
        DirPartyModel, LogisticsPostalAddressModel,
        extra=1, max_num=5, fields='__all__')

    if request.method == 'POST':
        # formulario enviado
        customer_form = CustomerForm(request.POST, instance=Customer)
        party_form = PartyForm(request.POST, instance=Party)

        if customer_form.is_valid() and party_form.is_valid():
            party = party_form.save()
            customer = customer_form.save(commit=False)
            customer.Party = party
            customer.save()
            messages.success(request, "Proveedor actualizado correctamente")

            electronic_formset = ElectronicFormSet(
                request.POST, prefix='efs', instance=Party)
            postal_formset = PostalFormSet(
                request.POST, prefix='pfs', instance=Party)

            for electronic_form in electronic_formset.forms:
                if electronic_form.is_valid():
                    description = electronic_form.cleaned_data.get(
                        'Description')
                    contact = electronic_form.cleaned_data.get('Contact')
                    if description and contact:
                        EA = electronic_form.save()
                        EA_list.append(EA.pk)
                else:
                    messages.warning(
                        request, 'Revise la información de contacto')

            if electronic_formset.is_valid():
                lea = LogisticsElectronicAddressModel.objects.filter(
                    Party=party)
                lea.exclude(pk__in=list(EA_list)).delete()

            for postal_form in postal_formset:
                if postal_form.is_valid():
                    description = postal_form.cleaned_data.get(
                        'Description')
                    if description:
                        PA = postal_form.save()
                        PA_list.append(PA.pk)
                else:
                    messages.warning(
                        request, 'Revise la información de dirección')

            if postal_formset.is_valid():
                lpa = LogisticsPostalAddressModel.objects.filter(Party=Party)
                lpa.exclude(pk__in=list(PA_list)).delete()

        else:
            electronic_formset = ElectronicFormSet(
                request.POST, prefix='efs')
            postal_formset = PostalFormSet(
                request.POST, prefix='pfs')
            messages.error(
                request, "Ocurrió un error al actualizar el proveedor")

    else:
        # formulario inicial
        customer_form = CustomerForm(instance=Customer)
        party_form = PartyForm(instance=Customer.Party)
        electronic_formset = ElectronicFormSet(
            prefix='efs', instance=Customer.Party)
        postal_formset = PostalFormSet(
            prefix='pfs', instance=Customer.Party)

    return render_to_response('customer/UpdateCustomer.html',
                              {'customer_form': customer_form,
                               'party_form': party_form,
                               'electronic_formset': electronic_formset,
                               'postal_formset': postal_formset,
                               'Customer': Customer, },
                              context_instance=RequestContext(request))


# CBV: View to delete an existing customer
# ----------------------------------------------------------------------------
class DeleteCustomerView(DeleteView):
    model = DirPartyModel
    template_name = 'customer/DeleteCustomer.html'
    success_url = '/customer'
    success_message = 'Se ha eliminado el proveedor'

    def delete(self, request, *args, **kwargs):
        """
        Calls the delete() method on the fetched object and then
        redirects to the success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request,
                         'Se ha eliminado el proveedor',
                         extra_tags='msg')
        return HttpResponseRedirect(success_url)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


# FBV: Export to csv
# ----------------------------------------------------------------------------
@login_required
def export_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="proveedores.csv"'

    writer = csv.writer(response)
    writer.writerow(['Número de cuenta',
                     'Nombre',
                     'Tipo de proveedor',
                     'RFC',
                     'Moneda',
                     'Direccion principal',
                     'Contacto principal'])
    customer_list = CustomerModel.objects.all()
    for customer in customer_list:
        writer.writerow([customer.AccountNum,
                         customer.Party.NameAlias,
                         customer.AccountType,
                         customer.VATNum,
                         customer.CurrencyCode,
                         customer.get_PrimaryAddress(),
                         customer.get_PrimaryElectronic()])

    return response


# FBV: Export to pdf
# ----------------------------------------------------------------------------
@login_required
def export_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    # pdf_name = "proveedores.pdf"  # llamado proveedores
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=landscape(letter),
                            rightMargin=20,
                            leftMargin=20,
                            topMargin=30,
                            bottomMargin=20,
                            )
    proveedores = []
    styles = getSampleStyleSheet()

    title = Paragraph("Listado de proveedores", styles['Heading2'])
    date = Paragraph(time.strftime("%d/%m/%Y"), styles['Heading2'])
    header = (title, date)
    t = Table([''] + [header] + [''])
    t.setStyle(TableStyle(
        [
            ('ALIGN', (1, 1), (1, 1), 'RIGHT'),
            ('TEXTCOLOR', (0, 1), (0, 0), colors.green),
        ]
    ))
    proveedores.append(t)

    headings = ('Número de cuenta', 'Nombre', 'Tipo de proveedor',
                'RFC', 'Moneda', 'Direccion principal', 'Contacto principal')
    customers = [(v.AccountNum, v.Party.NameAlias, v.AccountType,
                  v.VATNum, v.CurrencyCode, v.get_PrimaryAddress(),
                  v.get_PrimaryElectronic())
                 for v in CustomerModel.objects.all()]

    t = Table([headings] + customers)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (6, -1), 0.5, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 0.5, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))
    proveedores.append(t)
    doc.build(proveedores)
    response.write(buff.getvalue())
    buff.close()
    return response

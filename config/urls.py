#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-11-16 17:10:00
# @Last Modified by:   Alex
# @Last Modified time: 2016-01-04 15:35:51
"""Inventationery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from __future__ import unicode_literals
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views import defaults as default_views
from Inventationery.core.views import pdf_view

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),
    url(r'^', include('Inventationery.apps.login.urls')),
    url(r'^', include('Inventationery.apps.home.urls', namespace='home')),
    url(r'^', include('Inventationery.apps.Vendor.urls', namespace='vendor')),
    url(r'^', include('Inventationery.apps.PurchOrder.urls', namespace='purch')),
    url(r'^', include('Inventationery.apps.Inventory.urls', namespace='inventory')),
    url(r'^', include('Inventationery.apps.Payments.urls', namespace='payment')),
    url(r'^', include('Inventationery.apps.Company.urls', namespace='company')),
    url(r'^', include('Inventationery.apps.Customer.urls', namespace='customer')),
    url(r'^', include('Inventationery.apps.SalesOrder.urls', namespace='sales')),
    url(r'^quick_guide/$', pdf_view, name='guide'),

    url(r'^400/$', default_views.bad_request,
        kwargs={'exception': Exception("Bad Request!")}),
    url(r'^403/$', default_views.permission_denied,
        kwargs={'exception': Exception("Permissin Denied")}),
    url(r'^404/$', default_views.page_not_found,
        kwargs={'exception': Exception("Page not Found")}),
    url(r'^500/$', default_views.server_error),
    #(r'^search/', include('haystack.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'Inventationery admin'

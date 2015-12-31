#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmenta
# @Date:   2015-12-31 12:41:44
# @Last Modified by:   harmenta
# @Last Modified time: 2015-12-31 12:45:51

import datetime
from haystack import indexes
from .models import VendorModel


class VendorIndex(indexes.SearchIndex, indexes.Indexable):
    text_vendor = indexes.CharField(document=True, use_template=True)
    AccountNum = indexes.CharField(model_attr='AccountNum')
    Party = indexes.CharField(model_attr='Party')
    created_date = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return VendorModel

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(
            pub_date__lte=datetime.datetime.now())

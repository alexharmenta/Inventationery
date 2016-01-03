#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-12-20 22:05:42
# @Last Modified by:   Alex
# @Last Modified time: 2016-01-02 18:57:39
from django.db import models
from Inventationery.core.models import TimeStampedModel

# Create your models here.


# Class: Model for payment catalog
# ---------------------------------------------------------------------------
class PaymentModel(TimeStampedModel):
    PaymCode = models.CharField(max_length=5, blank=True, null=True)
    PaymName = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return "{0}" .format(self.PaymName)


# Class: Model for payment catalog
# ---------------------------------------------------------------------------
class PaymModeModel(TimeStampedModel):
    PaymModeCode = models.CharField(max_length=5, blank=True, null=True)
    PaymModeName = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return "{0}" .format(self.PaymModeName)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-12-20 22:05:42
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-20 22:09:01
from django.db import models
from Inventationery.core.models import TimeStampedModel

# Create your models here.


# Class: Model for payment catalog
# ---------------------------------------------------------------------------
class PaymentModel(TimeStampedModel):
    PaymCode = models.CharField(max_length=5)
    PaymName = models.CharField(max_length=50)

    def __unicode__(self):
        return "{0}" .format(self.PaymName)


# Class: Model for payment catalog
# ---------------------------------------------------------------------------
class PaymModeModel(TimeStampedModel):
    PaymModeCode = models.CharField(max_length=5)
    PaymModeName = models.CharField(max_length=50)

    def __unicode__(self):
        return "{0}" .format(self.PaymModeName)

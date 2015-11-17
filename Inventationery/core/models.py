#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: harmenta
# @Date:   2015-11-17 12:37:09
# @Last Modified by:   harmenta
# @Last Modified time: 2015-11-17 12:38:01
from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides selfupdating
    ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

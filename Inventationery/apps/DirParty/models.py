#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex Armenta
# @Date:   2015-11-16 19:08:22
# @Last Modified by:   harmenta
# @Last Modified time: 2015-11-23 10:54:02
from django.db import models
from Inventationery.core.models import TimeStampedModel


# Class: Model for DirParty
# ----------------------------------------------------------------------------
class DirPartyModel(TimeStampedModel):

    MALE = 'M'
    FEMALE = 'F'
    NOT_DEFINED = 'N'

    GENDER_CHOICES = (
        (MALE, 'Masculino'),
        (FEMALE, 'Femenino'),
        (NOT_DEFINED, 'No definido'),
    )

    # Party or Person
    Name = models.CharField(max_length=60)
    NameAlias = models.CharField(max_length=50, blank=True, null=True)
    LanguageCode = models.CharField(max_length=5, default='es-mx')
    # Person
    SecondName = models.CharField(max_length=30, blank=True, null=True)
    FirstLastName = models.CharField(max_length=30)
    SecondLastName = models.CharField(max_length=30, blank=True, null=True)
    Gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              default=NOT_DEFINED,)

    def __unicode__(self):
        return self.NameAlias

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0011_auto_20151122_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchlinemodel',
            name='LineNum',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
    ]

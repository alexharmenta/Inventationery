# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0004_purchordermodel_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchlinemodel',
            name='PurchPrice',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]

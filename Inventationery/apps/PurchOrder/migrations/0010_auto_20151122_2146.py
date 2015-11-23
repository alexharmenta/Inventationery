# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0009_auto_20151122_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchordermodel',
            name='SubTotal',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True),
        ),
    ]

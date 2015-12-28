# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0010_itemvendormodel_vendoritemid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemvendormodel',
            name='VendorPrice',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]

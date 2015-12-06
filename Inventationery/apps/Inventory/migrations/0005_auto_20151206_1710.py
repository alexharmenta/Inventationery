# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0004_auto_20151206_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorymodel',
            name='Qty',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

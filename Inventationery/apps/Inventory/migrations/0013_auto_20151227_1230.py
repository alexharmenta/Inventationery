# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0012_auto_20151227_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecoresproductmodel',
            name='Item',
            field=models.OneToOneField(null=True, default=None, blank=True, to='Inventory.ItemModel'),
        ),
    ]

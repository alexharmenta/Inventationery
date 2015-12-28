# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0009_movementhistorymodel_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemvendormodel',
            name='VendorItemId',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0006_remove_purchordermodel_invoiceaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchordermodel',
            name='Remarks',
            field=models.TextField(default=None, null=True, blank=True),
        ),
    ]

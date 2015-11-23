# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0005_auto_20151121_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchordermodel',
            name='InvoiceAccount',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0003_auto_20151121_1813'),
        ('PurchOrder', '0004_auto_20151120_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchordermodel',
            name='OrderAccount',
        ),
        migrations.AddField(
            model_name='purchordermodel',
            name='Vendor',
            field=models.ForeignKey(default=None, to='Vendor.VendorModel'),
        ),
    ]

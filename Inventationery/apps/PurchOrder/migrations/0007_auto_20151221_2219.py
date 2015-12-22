# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0006_auto_20151220_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchordermodel',
            name='PurchStatus',
            field=models.CharField(default=b'OPE', max_length=100),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0003_auto_20151120_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchordermodel',
            name='CashDisc',
        ),
        migrations.RemoveField(
            model_name='purchordermodel',
            name='CashDiscPercent',
        ),
    ]

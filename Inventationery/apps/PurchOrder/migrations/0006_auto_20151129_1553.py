# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0005_auto_20151128_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchordermodel',
            name='Enabled',
            field=models.NullBooleanField(default=True),
        ),
    ]

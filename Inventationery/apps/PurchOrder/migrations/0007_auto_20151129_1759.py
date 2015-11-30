# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0006_auto_20151129_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchordermodel',
            name='Enabled',
            field=models.BooleanField(default=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PurchOrder', '0003_auto_20151124_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchordermodel',
            name='Enabled',
            field=models.BooleanField(default=True),
        ),
    ]

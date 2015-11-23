# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
        ('PurchOrder', '0013_auto_20151122_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchlinemodel',
            name='ItemId',
        ),
        migrations.AddField(
            model_name='purchlinemodel',
            name='ItemId',
            field=models.ForeignKey(default=None, to='Inventory.InventModel'),
            preserve_default=False,
        ),
    ]

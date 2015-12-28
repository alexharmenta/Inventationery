# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0008_itemvendormodel_movementhistorymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='movementhistorymodel',
            name='Item',
            field=models.ForeignKey(related_name='ItemHistory', default=None, blank=True, to='Inventory.ItemModel', null=True),
        ),
    ]

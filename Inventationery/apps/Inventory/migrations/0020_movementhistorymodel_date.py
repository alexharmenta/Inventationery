# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0019_remove_itemmodel_unitid'),
    ]

    operations = [
        migrations.AddField(
            model_name='movementhistorymodel',
            name='Date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

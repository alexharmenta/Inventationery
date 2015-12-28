# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0020_movementhistorymodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmodel',
            name='ItemImage',
            field=models.ImageField(default=None, null=True, upload_to=b'ItemTable', blank=True),
        ),
    ]

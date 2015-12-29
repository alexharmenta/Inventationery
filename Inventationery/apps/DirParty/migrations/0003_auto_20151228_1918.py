# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DirParty', '0002_auto_20151224_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dirpartymodel',
            name='FirstLastName',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]

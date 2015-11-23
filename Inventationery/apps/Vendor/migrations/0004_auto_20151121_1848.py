# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0003_auto_20151121_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendormodel',
            name='Party',
            field=models.OneToOneField(related_name='VendorParty', default=None, to='DirParty.DirPartyModel'),
        ),
    ]

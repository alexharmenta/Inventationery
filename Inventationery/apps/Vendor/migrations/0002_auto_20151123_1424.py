# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendormodel',
            name='Party',
            field=models.OneToOneField(related_name='VendorParty', null=True, default=None, blank=True, to='DirParty.DirPartyModel'),
        ),
    ]

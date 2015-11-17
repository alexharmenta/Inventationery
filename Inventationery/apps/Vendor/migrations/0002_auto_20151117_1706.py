# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import Inventationery.apps.Vendor.models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendormodel',
            name='AccountNum',
            field=models.CharField(default=Inventationery.apps.Vendor.models.Get_Account_Num, unique=True, max_length=45),
        ),
    ]

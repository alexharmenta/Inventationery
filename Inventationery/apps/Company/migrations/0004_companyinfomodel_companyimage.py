# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0003_auto_20151228_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfomodel',
            name='CompanyImage',
            field=models.ImageField(default=None, null=True, upload_to=b'CompanyInfo', blank=True),
        ),
    ]

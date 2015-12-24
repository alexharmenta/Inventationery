# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfomodel',
            name='Description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='companyinfomodel',
            name='Email',
            field=models.EmailField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='companyinfomodel',
            name='Fax',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='companyinfomodel',
            name='Phone',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='companyinfomodel',
            name='URL',
            field=models.URLField(max_length=100, null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DirParty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dirpartymodel',
            name='Gender',
            field=models.CharField(default=b'N', max_length=1, null=True, blank=True, choices=[(b'M', b'Masculino'), (b'F', b'Femenino'), (b'N', b'No definido')]),
        ),
    ]

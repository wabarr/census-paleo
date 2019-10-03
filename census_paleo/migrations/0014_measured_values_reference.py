# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census_paleo', '0013_auto_20191003_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='measured_values',
            name='reference',
            field=models.ForeignKey(to='census_paleo.reference', null=True),
            preserve_default=True,
        ),
    ]

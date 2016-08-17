# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census_paleo', '0004_auto_20160817_1427'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='taxonomy',
            unique_together=set([('tclass', 'order', 'family', 'subfamily', 'tribe', 'genus', 'species', 'infraspecificEpithet', 'taxonRank', 'identificationQualifier')]),
        ),
    ]

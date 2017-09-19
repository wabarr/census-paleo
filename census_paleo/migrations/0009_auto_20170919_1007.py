# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census_paleo', '0008_functional_traits_trophic_reed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='functional_traits',
            name='locomotor_reed',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'A', b'arboreal'), (b'AT', b'arboreal-terrestrial'), (b'AQ', b'aquatic'), (b'S', b'subterranean'), (b'ST', b'subterranean-terrestrial'), (b'T', b'terrestrial'), (b'TA', b'terrestrial-aquatic')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census_paleo', '0010_functional_traits_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='functional_traits',
            name='locomotor_rowan',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'A', b'arboreal'), (b'AT', b'arboreal-terrestrial'), (b'AQ', b'aquatic'), (b'S', b'subterranean'), (b'ST', b'subterranean-terrestrial'), (b'T', b'terrestrial'), (b'TA', b'terrestrial-aquatic')]),
        ),
        migrations.AddField(
            model_name='functional_traits',
            name='trophic_rowan',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'B', b'leaves'), (b'C', b'meat'), (b'C/B', b'meat/bone'), (b'C/I', b'meat/invertebrates'), (b'FG', b'fresh grass'), (b'FL', b'fruit plus'), (b'G', b'grass'), (b'I', b'insects'), (b'MF', b'leaves and grass'), (b'OM', b'omnivorous'), (b'R', b'roots/bulbs')]),
        ),
    ]

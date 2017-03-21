# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census_paleo', '0006_auto_20160830_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='functional_traits',
            name='trophic_lintulaakso',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'C', b'Carnivore'), (b'P', b'Piscivore'), (b'M', b'Myrmecophage'), (b'MF', b'Mixed-Feeder'), (b'FG', b'Frugivore-Granivore'), (b'FH', b'Frugivore-Herbivore'), (b'FO', b'Frugivore-Omnivore'), (b'IO', b'Insectivore-Omnivore'), (b'I', b'Insectivore'), (b'G', b'Grazer'), (b'B', b'Browser')]),
            preserve_default=True,
        ),
    ]

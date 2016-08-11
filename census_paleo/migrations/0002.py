# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census_paleo',"0001_initial")
    ]

    operations = [
        migrations.CreateModel(
                    name='functional_traits',
                    fields=[
                        ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                        ('browse_graze', models.CharField(blank=True, max_length=100, null=True, choices=[(b'Grazer', b'Grazer'), (b'Browser', b'Browser'), (b'Mixed Feeder', b'Mixed Feeder')])),
                        ('habitat', models.CharField(blank=True, max_length=100, null=True, choices=[(b'Forest', b'Forest'), (b'Heavy Cover', b'Heavy Cover'), (b'Light Cover', b'Light Cover'), (b'Grassland', b'Grassland')])),
                        ('bodysize_brain_bunn', models.CharField(blank=True, max_length=100, null=True, choices=[(1, b'I: < 23 kg'), (2, b'II: 23 - 113 kg'), (3, b'III: 113 - 340 kg'), (4, b'IV: 340 - 907 kg'), (5, b'V: 907 - 2721 kg'), (6, b'VI: >2721 kg')])),
                        ('bodysize_lintulaakso', models.CharField(blank=True, max_length=100, null=True, choices=[(b'A', b'A: 0.5 - 8 kg'), (b'B', b'B: 8 - 45 kg'), (b'C', b'C: 45 - 90 kg'), (b'D', b'D: 90 - 180 kg'), (b'E', b'E: 180 - 360 kg'), (b'F', b'F: 360 + kg')])),
                        ('bodysize_species_mean_kg', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
                        ('locomotor_reed', models.CharField(blank=True, max_length=100, null=True, choices=[(b'A', b'arboreal'), (b'AT', b'arboreal-terrestrial'), (b'S', b'subterranean'), (b'ST', b'subterranean-terrestrial'), (b'T', b'terrestrial'), (b'TA', b'terrestrial-aquatic')])),
                        ('trophic_lintulaakso', models.CharField(blank=True, max_length=100, null=True, choices=[(b'C', b'Carnivore'), (b'P', b'Piscivore'), (b'M', b'Myrmecophage'), (b'FG', b'Frigivore-Granivore'), (b'FH', b'Frugivore-Herbivore'), (b'FO', b'Frugivore-Omnivore'), (b'IO', b'Insectivore-Omnivore'), (b'G', b'Grazer'), (b'B', b'Browser')])),
                    ],
                    options={
                        'db_table': 'functional_traits',
                    },
                    bases=(models.Model,),
                ),
        migrations.AddField(
            model_name='functional_traits',
            name='taxon',
            field=models.ForeignKey(to='census_paleo.taxonomy'),
            preserve_default=True,
        ),

    ]
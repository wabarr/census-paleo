# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census_paleo', '0012_add_rowan_traits'),
    ]

    operations = [
        migrations.CreateModel(
            name='measured_values',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.DecimalField(max_digits=20, decimal_places=5)),
            ],
            options={
                'db_table': 'measured_values',
                'verbose_name': 'measured value',
                'verbose_name_plural': 'measured values',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='measurement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('definition', models.CharField(max_length=200)),
                ('reference', models.ForeignKey(blank=True, to='census_paleo.reference', null=True)),
            ],
            options={
                'db_table': 'measurement',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='skeletal_element',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('notes', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'skeletal_element',
                'verbose_name': 'skeletal element',
                'verbose_name_plural': 'skeletal_elements',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='specimen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('museum', models.CharField(max_length=100)),
                ('collection_code', models.CharField(max_length=100)),
                ('specimen_number', models.CharField(max_length=100)),
                ('specimen_number_part', models.CharField(max_length=100, null=True, blank=True)),
                ('assemblage', models.ForeignKey(to='census_paleo.fossilLocation')),
                ('taxon', models.ForeignKey(to='census_paleo.taxonomy')),
            ],
            options={
                'db_table': 'specimen',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='measured_values',
            name='element',
            field=models.ForeignKey(to='census_paleo.skeletal_element'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='measured_values',
            name='measurement',
            field=models.ForeignKey(to='census_paleo.measurement'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='measured_values',
            name='specimen',
            field=models.ForeignKey(to='census_paleo.specimen'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='functional_traits',
            name='locomotor_rowan',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'T', b'terrestrial'), (b'AQ', b'aquatic'), (b'F', b'fossorial'), (b'A', b'arboreal'), (b'TA', b'terrestrial-arboreal')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='functional_traits',
            name='trophic_rowan',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'MF', b'Mixed-Feeder'), (b'MF-B', b'Mixed-Feeder / Browser'), (b'MF-FG', b'Mixed-Feeder / Frugivore-Granivore'), (b'FG', b'Frugivore-Granivore'), (b'MF-G', b'Mixed-Feeder / Grazer'), (b'B', b'Browser'), (b'OM', b'Omnivore'), (b'C', b'Carnivore'), (b'CI', b'Carnivore-Insectivore'), (b'CB', b'Carnivore-Bone'), (b'I', b'Insectivore'), (b'G', b'Grazer'), (b'FL', b'Fruit-Leaves'), (b'FB', b'Fruit-Browse'), (b'G-R', b'Grazer-Roots'), (b'OM-FL', b'Omnivore-Fruit/Leaves'), (b'OM-I', b'Omnivore-Insectivore'), (b'OM-C', b'Omnivore-Carnivore'), (b'FI', b'Fruit-Insects'), (b'F', b'Fruit'), (b'R', b'Roots')]),
            preserve_default=True,
        ),
    ]

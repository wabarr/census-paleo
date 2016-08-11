# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='censusLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullName', models.CharField(max_length=100)),
                ('shortName', models.CharField(unique=True, max_length=20)),
                ('country', models.CharField(max_length=100, choices=[(b'Algeria', b'Algeria'), (b'Angola', b'Angola'), (b'Benin', b'Benin'), (b'Botswana', b'Botswana'), (b'Burkina Faso', b'Burkina Faso'), (b'Burundi', b'Burundi'), (b'Cameroon', b'Cameroon'), (b'Cape Verde', b'Cape Verde'), (b'Central African Republic', b'Central African Republic'), (b'Chad', b'Chad'), (b'Congo, Democratic Republic of', b'Congo, Democratic Republic of'), (b'Cote dIvoire (Ivory Coast),', b'Cote dIvoire (Ivory Coast),'), (b'Djibouti', b'Djibouti'), (b'Egypt', b'Egypt'), (b'Equatorial Guinea', b'Equatorial Guinea'), (b'Eritrea', b'Eritrea'), (b'Ethiopia', b'Ethiopia'), (b'Gabon', b'Gabon'), (b'Gambia', b'Gambia'), (b'Ghana', b'Ghana'), (b'Guinea', b'Guinea'), (b'Guinea-Bissau', b'Guinea-Bissau'), (b'Kenya', b'Kenya'), (b'Lesotho', b'Lesotho'), (b'Liberia', b'Liberia'), (b'Libya', b'Libya'), (b'Madagascar', b'Madagascar'), (b'Malawi', b'Malawi'), (b'Mali', b'Mali'), (b'Mauritania', b'Mauritania'), (b'Mauritius', b'Mauritius'), (b'Morocco', b'Morocco'), (b'Mozambique', b'Mozambique'), (b'Namibia', b'Namibia'), (b'Niger', b'Niger'), (b'Nigeria', b'Nigeria'), (b'Rwanda', b'Rwanda'), (b'Sao Tome and Principe', b'Sao Tome and Principe'), (b'Senegal', b'Senegal'), (b'Seychelles', b'Seychelles'), (b'Sierra Leone', b'Sierra Leone'), (b'Somalia', b'Somalia'), (b'South Africa', b'South Africa'), (b'South Sudan', b'South Sudan'), (b'Sudan', b'Sudan'), (b'Swaziland', b'Swaziland'), (b'Tanzania', b'Tanzania'), (b'Togo', b'Togo'), (b'Tunisia', b'Tunisia'), (b'Western Sahara', b'Western Sahara'), (b'Uganda', b'Uganda'), (b'Zambia', b'Zambia'), (b'Zimbabwe', b'Zimbabwe')])),
                ('mmAveragePrecipitation', models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)),
                ('minAltitude', models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)),
                ('maxAltitude', models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)),
                ('latitude', models.DecimalField(null=True, max_digits=25, decimal_places=10, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=25, decimal_places=10, blank=True)),
                ('georefMethod', models.CharField(max_length=100, choices=[(b'None', b'None'), (b'Publication', b'Publication'), (b'GetLatLon.com', b'GetLatLon.com'), (b'GoogleEarth', b'GoogleEarth')])),
                ('datum', models.CharField(default=b'WGS84', max_length=100)),
                ('WDPAID', models.IntegerField(max_length=25, null=True, verbose_name=b'ID from the World Database on Protected Areas', blank=True)),
            ],
            options={
                'db_table': 'censusLocation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='fossilLocation',
            fields=[
                ('censuslocation_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='census_paleo.censusLocation')),
                ('projectArea', models.CharField(max_length=100)),
                ('formation', models.CharField(max_length=100)),
                ('member', models.CharField(max_length=100, null=True, blank=True)),
                ('submember', models.CharField(max_length=100, null=True, blank=True)),
                ('minAgeMa', models.DecimalField(null=True, max_digits=10, decimal_places=5, blank=True)),
                ('maxAgeMa', models.DecimalField(null=True, max_digits=10, decimal_places=5, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'fossilLocation',
            },
            bases=('census_paleo.censuslocation',),
        ),
        migrations.CreateModel(
            name='occurrence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('presenceAbsenceOnly', models.BooleanField(default=False, verbose_name=b'Abundance is unknown, but taxon is known to be present.')),
                ('abundance', models.IntegerField(max_length=100, null=True, blank=True)),
                ('issue', models.NullBooleanField(default=False)),
                ('notes', models.CharField(max_length=200, null=True, blank=True)),
                ('location', models.ForeignKey(to='census_paleo.censusLocation', null=True)),
            ],
            options={
                'db_table': 'occurrence',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='reference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('authorshortstring', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('journal', models.CharField(max_length=100, null=True, blank=True)),
                ('volume', models.IntegerField(max_length=5, null=True, blank=True)),
                ('issue', models.IntegerField(max_length=5, null=True, blank=True)),
                ('pages', models.CharField(max_length=20, null=True, blank=True)),
                ('doi', models.CharField(max_length=100, null=True, blank=True)),
                ('dataEntryComplete', models.NullBooleanField(default=False)),
            ],
            options={
                'db_table': 'reference',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='taxonomy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kingdom', models.CharField(default=b'Animalia', max_length=100, null=True, blank=True, choices=[(b'Animalia', b'Animalia')])),
                ('phylum', models.CharField(default=b'Chordata', max_length=100, null=True, blank=True, choices=[(b'Chordata', b'Chordata')])),
                ('tclass', models.CharField(blank=True, max_length=100, null=True, verbose_name=b'class', choices=[(b'Mammalia', b'Mammalia'), (b'Reptilia', b'Reptilia'), (b'Pisces', b'Pisces'), (b'Aves', b'Aves'), (b'Amphibia', b'Amphibia')])),
                ('order', models.CharField(blank=True, max_length=100, null=True, choices=[(b'ARTIODACTYLA', b'ARTIODACTYLA'), (b'CARNIVORA', b'CARNIVORA'), (b'PERISSODACTYLA', b'PERISSODACTYLA'), (b'PRIMATES', b'PRIMATES'), (b'PROBOSCIDEA', b'PROBOSCIDEA'), (b'RODENTIA', b'RODENTIA'), (b'AFROSORICIDA', b'AFROSORICIDA'), (b'CETACEA', b'CETACEA'), (b'CHIROPTERA', b'CHIROPTERA'), (b'CINGULATA', b'CINGULATA'), (b'DASYUROMORPHIA', b'DASYUROMORPHIA'), (b'DERMOPTERA', b'DERMOPTERA'), (b'DIDELPHIMORPHIA', b'DIDELPHIMORPHIA'), (b'DIPROTODONTIA', b'DIPROTODONTIA'), (b'ERINACEOMORPHA', b'ERINACEOMORPHA'), (b'HYRACOIDEA', b'HYRACOIDEA'), (b'LAGOMORPHA', b'LAGOMORPHA'), (b'MACROSCELIDEA', b'MACROSCELIDEA'), (b'MICROBIOTHERIA', b'MICROBIOTHERIA'), (b'MONOTREMATA', b'MONOTREMATA'), (b'NOTORYCTEMORPHIA', b'NOTORYCTEMORPHIA'), (b'PAUCITUBERCULATA', b'PAUCITUBERCULATA'), (b'PERAMELEMORPHIA', b'PERAMELEMORPHIA'), (b'PHOLIDOTA', b'PHOLIDOTA'), (b'PILOSA', b'PILOSA'), (b'SCANDENTIA', b'SCANDENTIA'), (b'SIRENIA', b'SIRENIA'), (b'SORICOMORPHA', b'SORICOMORPHA'), (b'TUBULIDENTATA', b'TUBULIDENTATA')])),
                ('family', models.CharField(max_length=100, null=True, blank=True)),
                ('subFamily', models.CharField(max_length=100, null=True, blank=True)),
                ('tribe', models.CharField(blank=True, max_length=100, null=True, choices=[(b'Tragelaphini', b'Tragelaphini'), (b'Cephalophini', b'Cephalophini'), (b'Bovini', b'Bovini'), (b'Hippotragini', b'Hippotragini'), (b'Reduncini', b'Reduncini'), (b'Alcelaphini', b'Alcelaphini'), (b'Antilopini', b'Antilopini'), (b'Aepycerotini', b'Aepycerotini'), (b'Neotragini', b'Neotragini')])),
                ('genusName', models.CharField(max_length=100, null=True, verbose_name=b'genus', blank=True)),
                ('specificEpithet', models.CharField(max_length=100, null=True, verbose_name=b'species', blank=True)),
                ('infraspecificEpithet', models.CharField(max_length=100, null=True, blank=True)),
                ('identificationQualifier', models.CharField(max_length=100, null=True, blank=True)),
                ('extant', models.BooleanField()),
                ('commonName', models.CharField(max_length=100, null=True, blank=True)),
                ('synonyms', models.CharField(max_length=2000, null=True, blank=True)),
                ('taxonRank', models.CharField(max_length=100, null=True, choices=[(b'CLASS', b'CLASS'), (b'ORDER', b'ORDER'), (b'FAMILY', b'FAMILY'), (b'SUBFAMILY', b'SUBFAMILY'), (b'TRIBE', b'TRIBE'), (b'GENUS', b'GENUS'), (b'SPECIES', b'SPECIES'), (b'SUBSPECIES', b'SUBSPECIES'), (b'INFRAORDER', b'INFRAORDER'), (b'SUBGENUS', b'SUBGENUS'), (b'SUBORDER', b'SUBORDER'), (b'SUPERFAMILY', b'SUPERFAMILY')])),
                ('Fernandez_Vrba_2005_Name', models.CharField(max_length=255, null=True, blank=True)),
                ('BinindaEmonds_2008_Name', models.CharField(max_length=255, null=True, blank=True)),
                ('ref', models.ForeignKey(to='census_paleo.reference')),
            ],
            options={
                'db_table': 'taxonomy',
                'verbose_name': 'taxon',
                'verbose_name_plural': 'taxa',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='occurrence',
            name='ref',
            field=models.ForeignKey(to='census_paleo.reference', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='occurrence',
            name='taxon',
            field=models.ForeignKey(to='census_paleo.taxonomy', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='occurrence',
            unique_together=set([('location', 'taxon', 'ref')]),
        ),
        migrations.AddField(
            model_name='fossillocation',
            name='geologyRef',
            field=models.ForeignKey(to='census_paleo.reference'),
            preserve_default=True,
        ),
    ]

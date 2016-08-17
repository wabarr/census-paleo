# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census_paleo', '0001_auto_20160811_1119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='functional_traits',
            options={'verbose_name': 'functional trait', 'verbose_name_plural': 'functional traits'},
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='presenceAbsenceOnly',
            field=models.BooleanField(default=False, verbose_name=b'Present'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taxonomy',
            name='order',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'AFROSORICIDA', b'AFROSORICIDA'), (b'ARTIODACTYLA', b'ARTIODACTYLA'), (b'CARNIVORA', b'CARNIVORA'), (b'PERISSODACTYLA', b'PERISSODACTYLA'), (b'PRIMATES', b'PRIMATES'), (b'PROBOSCIDEA', b'PROBOSCIDEA'), (b'RODENTIA', b'RODENTIA'), (b'AFROSORICIDA', b'AFROSORICIDA'), (b'CETACEA', b'CETACEA'), (b'CHIROPTERA', b'CHIROPTERA'), (b'CINGULATA', b'CINGULATA'), (b'DASYUROMORPHIA', b'DASYUROMORPHIA'), (b'DERMOPTERA', b'DERMOPTERA'), (b'DIDELPHIMORPHIA', b'DIDELPHIMORPHIA'), (b'DIPROTODONTIA', b'DIPROTODONTIA'), (b'ERINACEOMORPHA', b'ERINACEOMORPHA'), (b'HYRACOIDEA', b'HYRACOIDEA'), (b'LAGOMORPHA', b'LAGOMORPHA'), (b'MACROSCELIDEA', b'MACROSCELIDEA'), (b'MICROBIOTHERIA', b'MICROBIOTHERIA'), (b'MONOTREMATA', b'MONOTREMATA'), (b'NOTORYCTEMORPHIA', b'NOTORYCTEMORPHIA'), (b'PAUCITUBERCULATA', b'PAUCITUBERCULATA'), (b'PERAMELEMORPHIA', b'PERAMELEMORPHIA'), (b'PHOLIDOTA', b'PHOLIDOTA'), (b'PILOSA', b'PILOSA'), (b'SCANDENTIA', b'SCANDENTIA'), (b'SIRENIA', b'SIRENIA'), (b'SORICOMORPHA', b'SORICOMORPHA'), (b'TUBULIDENTATA', b'TUBULIDENTATA')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taxonomy',
            name='tribe',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'Tragelaphini', b'Tragelaphini'), (b'Cephalophini', b'Cephalophini'), (b'Bovini', b'Bovini'), (b'Hippotragini', b'Hippotragini'), (b'Reduncini', b'Reduncini'), (b'Alcelaphini', b'Alcelaphini'), (b'Antilopini', b'Antilopini'), (b'Aepycerotini', b'Aepycerotini'), (b'Neotragini', b'Neotragini'), (b'Colobini', b'Colobini'), (b'Papionini', b'Papionini'), (b'Hominini', b'Hominini')]),
            preserve_default=True,
        ),
    ]

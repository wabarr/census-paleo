# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census_paleo', '0005_auto_20160817_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='fossillocation',
            name='locality',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='censuslocation',
            name='country',
            field=models.CharField(max_length=100, choices=[(b'Afghanistan', b'Afghanistan'), (b'Algeria', b'Algeria'), (b'Angola', b'Angola'), (b'Anguilla', b'Anguilla'), (b'Antigua and Barbuda', b'Antigua and Barbuda'), (b'Argentina', b'Argentina'), (b'Armenia', b'Armenia'), (b'Aruba', b'Aruba'), (b'Australia', b'Australia'), (b'Azerbaijan', b'Azerbaijan'), (b'Bahamas', b'Bahamas'), (b'Bahrain', b'Bahrain'), (b'Bangladesh', b'Bangladesh'), (b'Barbados', b'Barbados'), (b'Belize', b'Belize'), (b'Benin', b'Benin'), (b'Bermuda', b'Bermuda'), (b'Bhutan', b'Bhutan'), (b'Bolivia', b'Bolivia'), (b'Botswana', b'Botswana'), (b'Brazil', b'Brazil'), (b'British Virgin Islands', b'British Virgin Islands'), (b'Brunei', b'Brunei'), (b'Burkina Faso', b'Burkina Faso'), (b'Burundi', b'Burundi'), (b'Cambodia', b'Cambodia'), (b'Cameroon', b'Cameroon'), (b'Canada', b'Canada'), (b'Cape Verde', b'Cape Verde'), (b'Cayman Islands', b'Cayman Islands'), (b'Central African Republic', b'Central African Republic'), (b'Chad', b'Chad'), (b'Chile', b'Chile'), (b'China', b'China'), (b'Colombia', b'Colombia'), (b'Congo, Democratic Republic of', b'Congo, Democratic Republic of'), (b'Costa Rica', b'Costa Rica'), (b'Cote dIvoire (Ivory Coast),', b'Cote dIvoire (Ivory Coast),'), (b'Cuba', b'Cuba'), (b'Djibouti', b'Djibouti'), (b'Dominica', b'Dominica'), (b'Dominican Republic', b'Dominican Republic'), (b'Ecuador', b'Ecuador'), (b'Egypt', b'Egypt'), (b'El Salvador', b'El Salvador'), (b'Equatorial Guinea', b'Equatorial Guinea'), (b'Eritrea', b'Eritrea'), (b'Ethiopia', b'Ethiopia'), (b'French Guiana', b'French Guiana'), (b'Gabon', b'Gabon'), (b'Gambia', b'Gambia'), (b'Ghana', b'Ghana'), (b'Grenada', b'Grenada'), (b'Guadeloupe', b'Guadeloupe'), (b'Guatemala', b'Guatemala'), (b'Guinea-Bissau', b'Guinea-Bissau'), (b'Guinea', b'Guinea'), (b'Guyana', b'Guyana'), (b'Haiti', b'Haiti'), (b'Honduras', b'Honduras'), (b'India', b'India'), (b'Indonesia', b'Indonesia'), (b'Iran', b'Iran'), (b'Iraq', b'Iraq'), (b'Israel', b'Israel'), (b'Jamaica', b'Jamaica'), (b'Japan', b'Japan'), (b'Jordan', b'Jordan'), (b'Kazakhstan', b'Kazakhstan'), (b'Kenya', b'Kenya'), (b'Kuwait', b'Kuwait'), (b'Kyrgyzstan', b'Kyrgyzstan'), (b'Laos', b'Laos'), (b'Lebanon', b'Lebanon'), (b'Lesotho', b'Lesotho'), (b'Liberia', b'Liberia'), (b'Libya', b'Libya'), (b'Madagascar', b'Madagascar'), (b'Malawi', b'Malawi'), (b'Malaysia', b'Malaysia'), (b'Maldives', b'Maldives'), (b'Mali', b'Mali'), (b'Martinique', b'Martinique'), (b'Mauritania', b'Mauritania'), (b'Mauritius', b'Mauritius'), (b'Mexico', b'Mexico'), (b'Mongolia', b'Mongolia'), (b'Montserrat', b'Montserrat'), (b'Morocco', b'Morocco'), (b'Mozambique', b'Mozambique'), (b'Myanmar', b'Myanmar'), (b'Namibia', b'Namibia'), (b'Nepal', b'Nepal'), (b'Netherlands Antilles', b'Netherlands Antilles'), (b'Nicaragua', b'Nicaragua'), (b'Niger', b'Niger'), (b'Nigeria', b'Nigeria'), (b'North Korea', b'North Korea'), (b'Oman', b'Oman'), (b'Pakistan', b'Pakistan'), (b'Panama', b'Panama'), (b'Paraguay', b'Paraguay'), (b'Peru', b'Peru'), (b'Philippines', b'Philippines'), (b'Puerto Rico', b'Puerto Rico'), (b'Qatar', b'Qatar'), (b'Rwanda', b'Rwanda'), (b'Saint Kitts and Nevis', b'Saint Kitts and Nevis'), (b'Saint Lucia', b'Saint Lucia'), (b'Saint Vincent and the Grenadines', b'Saint Vincent and the Grenadines'), (b'Sao Tome and Principe', b'Sao Tome and Principe'), (b'Saudi Arabia', b'Saudi Arabia'), (b'Senegal', b'Senegal'), (b'Seychelles', b'Seychelles'), (b'Sierra Leone', b'Sierra Leone'), (b'Singapore', b'Singapore'), (b'Somalia', b'Somalia'), (b'South Africa', b'South Africa'), (b'South Korea', b'South Korea'), (b'South Sudan', b'South Sudan'), (b'Sri Lanka', b'Sri Lanka'), (b'Sudan', b'Sudan'), (b'Suriname', b'Suriname'), (b'Swaziland', b'Swaziland'), (b'Syria', b'Syria'), (b'Taiwan', b'Taiwan'), (b'Tajikistan', b'Tajikistan'), (b'Tanzania', b'Tanzania'), (b'Thailand', b'Thailand'), (b'Timor-Leste', b'Timor-Leste'), (b'Togo', b'Togo'), (b'Trinidad and Tobago', b'Trinidad and Tobago'), (b'Tunisia', b'Tunisia'), (b'Turkmenistan', b'Turkmenistan'), (b'Uganda', b'Uganda'), (b'United Arab Emirates', b'United Arab Emirates'), (b'United States', b'United States'), (b'Uruguay', b'Uruguay'), (b'US Virgin Islands', b'US Virgin Islands'), (b'Uzbekistan', b'Uzbekistan'), (b'Venezuela', b'Venezuela'), (b'Vietnam', b'Vietnam'), (b'Western Sahara', b'Western Sahara'), (b'Yemen', b'Yemen'), (b'Zambia', b'Zambia'), (b'Zimbabwe', b'Zimbabwe')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='presenceAbsenceOnly',
            field=models.BooleanField(default=True, verbose_name=b'Present'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='taxonomy',
            name='tribe',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'Tragelaphini', b'Tragelaphini'), (b'Cephalophini', b'Cephalophini'), (b'Bovini', b'Bovini'), (b'Hippotragini', b'Hippotragini'), (b'Reduncini', b'Reduncini'), (b'Alcelaphini', b'Alcelaphini'), (b'Antilopini', b'Antilopini'), (b'Aepycerotini', b'Aepycerotini'), (b'Neotragini', b'Neotragini'), (b'Colobini', b'Colobini'), (b'Papionini', b'Papionini'), (b'Hominini', b'Hominini'), (b'Boselaphini', b'Boselaphini'), (b'Caprini', b'Caprini'), (b'Giraffini', b'Giraffini'), (b'Palaeotragini', b'Palaeotragini'), (b'Sivatheriini', b'Sivatheriini'), (b'Kubanochoerini', b'Kubanochoerini'), (b'Nyanzachoerini', b'Nyanzachoerini'), (b'Phacochoerini', b'Phacochoerini'), (b'Potamochoerini', b'Potamochoerini'), (b'Homotheriini', b'Homotheriini'), (b'Metailurini', b'Metailurini'), (b'Smilodontini', b'Smilodontini'), (b'Enhydrini', b'Enhydrini'), (b'Protoxerini', b'Protoxerini')]),
            preserve_default=True,
        ),
    ]

from django.db import models
from django.core.exceptions import ValidationError

class reference(models.Model):
    authorshortstring = models.CharField(max_length=100)
    year = models.IntegerField()
    journal = models.CharField(max_length=100, blank=True, null=True)
    volume = models.IntegerField(max_length=5, blank=True, null=True)
    issue = models.IntegerField(max_length=5, blank=True, null=True)
    pages = models.CharField(max_length=20, blank=True, null=True)
    doi = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        name = self.authorshortstring + ", " + str(self.year)
        return name

    class Meta:
        db_table = 'reference'

# #choices for upcoming taxonomy class
CHOICES_KINGDOM = (
("Animalia", "Animalia"),
)

CHOICES_PHYLUM = (
("Chordata", "Chordata"),
)

CHOICES_CLASS = (
("Mammalia", "Mammalia"),
("Reptilia", "Reptilia"),
("Pisces", "Pisces"),
("Aves", "Aves"),
("Amphibia", "Amphibia"),
)

CHOICES_ORDER = (
("ARTIODACTYLA", "ARTIODACTYLA"),
("CARNIVORA", "CARNIVORA"),
("PERISSODACTYLA", "PERISSODACTYLA"),
("PRIMATES", "PRIMATES"),
("PROBOSCIDEA", "PROBOSCIDEA"),
("RODENTIA", "RODENTIA"),
("AFROSORICIDA", "AFROSORICIDA"),
("CETACEA", "CETACEA"),
("CHIROPTERA", "CHIROPTERA"),
("CINGULATA", "CINGULATA"),
("DASYUROMORPHIA", "DASYUROMORPHIA"),
("DERMOPTERA", "DERMOPTERA"),
("DIDELPHIMORPHIA", "DIDELPHIMORPHIA"),
("DIPROTODONTIA", "DIPROTODONTIA"),
("ERINACEOMORPHA", "ERINACEOMORPHA"),
("HYRACOIDEA", "HYRACOIDEA"),
("LAGOMORPHA", "LAGOMORPHA"),
("MACROSCELIDEA", "MACROSCELIDEA"),
("MICROBIOTHERIA", "MICROBIOTHERIA"),
("MONOTREMATA", "MONOTREMATA"),
("NOTORYCTEMORPHIA", "NOTORYCTEMORPHIA"),
("PAUCITUBERCULATA", "PAUCITUBERCULATA"),
("PERAMELEMORPHIA", "PERAMELEMORPHIA"),
("PHOLIDOTA", "PHOLIDOTA"),
("PILOSA", "PILOSA"),
("SCANDENTIA", "SCANDENTIA"),
("SIRENIA", "SIRENIA"),
("SORICOMORPHA", "SORICOMORPHA"),
("TUBULIDENTATA", "TUBULIDENTATA"),

)

CHOICES_RANK = (
('CLASS', 'CLASS'),
('ORDER', 'ORDER'),
('FAMILY', 'FAMILY'),
('SUBFAMILY', 'SUBFAMILY'),
('TRIBE', 'TRIBE'),
('GENUS', 'GENUS'),
('SPECIES', 'SPECIES'),
('SUBSPECIES', 'SUBSPECIES'),
('INFRAORDER', 'INFRAORDER'),
('SUBGENUS', 'SUBGENUS'),
('SUBORDER', 'SUBORDER'),
('SUPERFAMILY', 'SUPERFAMILY'),
)

CHOICES_tribe = (
("Tragelaphini", "Tragelaphini"),
("Cephalophini", "Cephalophini"),
("Bovini", "Bovini"),
("Hippotragini", "Hippotragini"),
("Reduncini", "Reduncini"),
("Alcelaphini", "Alcelaphini"),
("Antilopini", "Antilopini"),
("Aepycerotini", "Aepycerotini"),
("Neotragini", "Neotragini"),
)


class taxonomy(models.Model):
    kingdom = models.CharField(max_length=100, null=True, blank=True, choices=CHOICES_KINGDOM, default="Animalia")
    phylum = models.CharField(max_length=100, null=True, blank=True, choices=CHOICES_PHYLUM, default="Chordata")
    tclass = models.CharField(max_length=100, null=True, blank=True, choices=CHOICES_CLASS, verbose_name="class")
    order = models.CharField(max_length=100, null=True, blank=True, choices=CHOICES_ORDER)
    family = models.CharField(max_length=100, null=True, blank=True)
    subFamily = models.CharField(max_length=100, null=True, blank=True)
    tribe = models.CharField(max_length=100, null=True, blank=True, choices=CHOICES_tribe)
    genusName = models.CharField(max_length=100, null=True, blank=True, verbose_name = "genus")
    specificEpithet = models.CharField(max_length=100, null=True, blank=True, verbose_name = "species")
    infraspecificEpithet = models.CharField(max_length=100, null=True, blank=True)
    identificationQualifier = models.CharField(max_length=100, null=True, blank=True)
    extant = models.BooleanField()
    commonName = models.CharField(max_length=100, null=True, blank=True)
    synonyms = models.CharField(max_length=2000, null=True, blank=True)
    taxonRank = models.CharField(max_length=100, null=True, blank=False, choices=CHOICES_RANK)
    ref = models.ForeignKey(reference)
    Fernandez_Vrba_2005_Name = models.CharField(max_length=255, null=True, blank=True)
    BinindaEmonds_2008_Name = models.CharField(max_length=255, null=True, blank=True)


    class Meta:
        db_table = 'taxonomy'
        verbose_name = "taxon"
        verbose_name_plural = "taxa"

    def __unicode__(self):
        if str(self.taxonRank).lower() == 'class':
            name =  self.tclass + " (" + self.taxonRank + ")"
        elif str(self.taxonRank).lower() == 'order':
            name =  self.order + " (" + self.taxonRank + ")"
        elif str(self.taxonRank).lower() == 'family':
            name =  self.family + " (" + self.taxonRank + ")"
        elif str(self.taxonRank).lower() == 'subfamily':
            name =   self.subFamily + " (" + self.taxonRank + ")"
        elif str(self.taxonRank).lower() == 'tribe':
            name =   self.tribe + " (" + self.taxonRank + ")"
        elif str(self.taxonRank).lower() == 'genus':
            name =   self.genusName + " (" + self.taxonRank + ")"
        elif str(self.taxonRank).lower() == 'species':
            name =   self.genusName + " " + self.specificEpithet + " (" + self.taxonRank + ")"
        elif str(self.taxonRank).lower() == 'subspecies':
            name =  self.genusName + " " + self.specificEpithet + " " + self.infraspecificEpithet + " (" + self.taxonRank + ")"
        else:
            name =  " "

        if self.identificationQualifier:
            name = self.identificationQualifier + " " + name

        if not self.extant:
            name += " **"

        return name


CHOICES_georefMethod = (
('None', 'None'),
('Publication', 'Publication'),
('GetLatLon.com', 'GetLatLon.com'),
('GoogleEarth', 'GoogleEarth'),
)

CHOICES_AfricanCountry = (
("Algeria", "Algeria"),
("Angola", "Angola"),
("Benin", "Benin"),
("Botswana", "Botswana"),
("Burkina Faso", "Burkina Faso"),
("Burundi", "Burundi"),
("Cameroon", "Cameroon"),
("Cape Verde", "Cape Verde"),
("Central African Republic", "Central African Republic"),
("Chad", "Chad"),
("Congo, Democratic Republic of", "Congo, Democratic Republic of"),
("Cote dIvoire (Ivory Coast),", "Cote dIvoire (Ivory Coast),"),
("Djibouti", "Djibouti"),
("Egypt", "Egypt"),
("Equatorial Guinea", "Equatorial Guinea"),
("Eritrea", "Eritrea"),
("Ethiopia", "Ethiopia"),
("Gabon", "Gabon"),
("Gambia", "Gambia"),
("Ghana", "Ghana"),
("Guinea", "Guinea"),
("Guinea-Bissau", "Guinea-Bissau"),
("Kenya", "Kenya"),
("Lesotho", "Lesotho"),
("Liberia", "Liberia"),
("Libya", "Libya"),
("Madagascar", "Madagascar"),
("Malawi", "Malawi"),
("Mali", "Mali"),
("Mauritania", "Mauritania"),
("Mauritius", "Mauritius"),
("Morocco", "Morocco"),
("Mozambique", "Mozambique"),
("Namibia", "Namibia"),
("Niger", "Niger"),
("Nigeria", "Nigeria"),
("Rwanda", "Rwanda"),
("Sao Tome and Principe", "Sao Tome and Principe"),
("Senegal", "Senegal"),
("Seychelles", "Seychelles"),
("Sierra Leone", "Sierra Leone"),
("Somalia", "Somalia"),
("South Africa", "South Africa"),
("South Sudan", "South Sudan"),
("Sudan", "Sudan"),
("Swaziland", "Swaziland"),
("Tanzania", "Tanzania"),
("Togo", "Togo"),
("Tunisia", "Tunisia"),
("Western Sahara", "Western Sahara"),
("Uganda", "Uganda"),
("Zambia", "Zambia"),
("Zimbabwe", "Zimbabwe"),
)


class censusLocation(models.Model):
    fullName = models.CharField(max_length=100)
    shortName = models.CharField(max_length=20, unique=True)
    country = models.CharField(max_length=100, choices=CHOICES_AfricanCountry)
    mmAveragePrecipitation = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    minAltitude = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    maxAltitude = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    latitude = models.DecimalField(max_digits=25, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=25, decimal_places=10, null=True, blank=True)
    georefMethod = models.CharField(max_length=100, choices=CHOICES_georefMethod)
    datum = models.CharField(max_length=100, default="WGS84")

    class Meta:
        db_table = 'censusLocation'

    def __unicode__(self):
        return self.shortName

class fossilLocation(censusLocation):
    projectArea = member = models.CharField(max_length=100)
    formation = models.CharField(max_length=100)
    member = models.CharField(max_length=100, null=True, blank=True)
    submember = models.CharField(max_length=100, null=True, blank=True)
    minAgeMa = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)
    maxAgeMa = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)
    geologyRef = models.ForeignKey(reference)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'fossilLocation'
    def __unicode__(self):
        return self.projectArea + " - " + self.member + " - " + self.submember


class occurrence(models.Model):
    ref = models.ForeignKey(reference, null=True, blank=False, )
    location = models.ForeignKey(censusLocation, null=True, blank=False)
    taxon = models.ForeignKey(taxonomy, null=True, blank=False)
    presenceAbsenceOnly = models.BooleanField(default=False, verbose_name="Abundance is unknown, but taxon is known to be present.")
    abundance = models.IntegerField(max_length=100, null=True, blank=True)
    issue = models.NullBooleanField(default=False)
    notes = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'occurrence'
        unique_together = ["location", "taxon", "ref"]

    def __unicode__(self):
        return str(self.location) + "_" + str(self.taxon) + "=" + str(self.abundance)

    def clean(self):
        if self.presenceAbsenceOnly and self.abundance:
            raise ValidationError("You cannot enter an abundance value and also indicate that the data is presence/absence only.")
        if self.presenceAbsenceOnly and self.abundance == 0:
            raise ValidationError("You indicated that the data is presence/absence only. You should enter a blank for abundance, not a zero.")
        if not self.presenceAbsenceOnly and not self.abundance:
            raise ValidationError("You must EITHER enter an abundance value OR indicate that the data is presence/absence only.")
        if self.issue and not self.notes:
            raise ValidationError("You said there was an issue with this data...so you must include some details in the notes field")
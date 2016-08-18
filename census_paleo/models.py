# -*- coding: utf-8 -*-
from django.db import models
from django.core.exceptions import ValidationError
from choices_functional_trait import *
from choices_models import *
from choices_taxonomy import *
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import NON_FIELD_ERRORS

class reference(models.Model):
    authorshortstring = models.CharField(max_length=100)
    year = models.IntegerField()
    journal = models.CharField(max_length=100, blank=True, null=True)
    volume = models.IntegerField(max_length=5, blank=True, null=True)
    issue = models.IntegerField(max_length=5, blank=True, null=True)
    pages = models.CharField(max_length=20, blank=True, null=True)
    doi = models.CharField(max_length=100, blank=True, null=True)
    dataEntryComplete = models.NullBooleanField(blank=True, default=False)

    def __unicode__(self):
        # if self.dataEntryComplete:
        #     name = self.authorshortstring + ", " + str(self.year) + " - Data Entry Complete"
        # else:
        #     name = self.authorshortstring + ", " + str(self.year)
        name = self.authorshortstring + ", " + str(self.year)
        return name

    class Meta:
        db_table = 'reference'


class taxonomy(models.Model):
    kingdom = models.CharField(max_length=100, null=True, blank=True, choices=CHOICES_KINGDOM, default="Animalia")
    phylum = models.CharField(max_length=100, null=True, blank=True, choices=CHOICES_PHYLUM, default="Chordata")
    tclass = models.CharField(max_length=100, null=True, blank=True, choices=CHOICES_CLASS, verbose_name="class")
    order = models.CharField(max_length=100, null=True, blank=True, choices=CHOICES_ORDER)
    family = models.CharField(max_length=100, null=True, blank=True)
    subfamily = models.CharField(max_length=100, null=True, blank=True)
    tribe = models.CharField(max_length=100, null=True, blank=True, choices=CHOICES_tribe)
    genus = models.CharField(max_length=100, null=True, blank=True, verbose_name = "genus")
    species = models.CharField(max_length=100, null=True, blank=True, verbose_name = "species")
    infraspecificEpithet = models.CharField(max_length=100, null=True, blank=True)
    identificationQualifier = models.CharField(max_length=100, null=True, blank=True)
    extant = models.BooleanField()
    commonName = models.CharField(max_length=100, null=True, blank=True)
    synonyms = models.CharField(max_length=2000, null=True, blank=True)
    taxonRank = models.CharField(max_length=100, null=True, blank=False, choices=CHOICES_RANK)
    ref = models.ForeignKey(reference)
    Fernandez_Vrba_2005_Name = models.CharField(max_length=255, null=True, blank=True)
    BinindaEmonds_2008_Name = models.CharField(max_length=255, null=True, blank=True)
    #habitat = models.CharField(max_length=25, null=True, blank=True, choices = CHOICES_HABITAT)
    #diet = models.CharField(max_length=25, null=True, blank=True, choices = CHOICES_DIET)


    class Meta:
        db_table = 'taxonomy'
        verbose_name = "taxon"
        verbose_name_plural = "taxa"
        unique_together = ['tclass','order','family','subfamily','tribe','genus','species','infraspecificEpithet','taxonRank','identificationQualifier']

    def __unicode__(self):
        if str(self.taxonRank).lower() == 'tclass':
            name =  self.tclass + " (class)"
        elif str(self.taxonRank).lower() == 'order':
            name =  self.order + " (" + self.taxonRank + ")"
        elif str(self.taxonRank).lower() == 'family':
            name =  self.family + " (" + self.taxonRank + ")"
        elif str(self.taxonRank).lower() == 'subfamily':
            name =   self.subfamily + " (" + self.taxonRank + ")"
        elif str(self.taxonRank).lower() == 'tribe':
            name =   self.tribe + " (" + self.taxonRank + ")"
        elif str(self.taxonRank).lower() == 'genus':
            name =   self.genus + " (" + self.taxonRank + ")"
        elif str(self.taxonRank).lower() == 'species':
            name =   self.genus + " " + self.species + " (" + self.taxonRank + ")"
        elif str(self.taxonRank).lower() == 'subspecies':
            name =  self.genus + " " + self.species + " " + self.infraspecificEpithet + " (" + self.taxonRank + ")"
        else:
            name =  " (" + self.taxonRank + ")"

        if self.identificationQualifier:
            name = self.identificationQualifier + " " + name

        if not self.extant:
            name += u" ✝"

        return name

    def validate_implied_taxon(self,rankString, **kwargs):
        modelFieldName = kwargs.keys()[0] #need to do some tests here!
        if getattr(self,modelFieldName):
            try:
                taxonomy.objects.get(taxonRank=rankString, **kwargs)
            except ObjectDoesNotExist:
                raise ValidationError(
                    "This taxon implies the existence of '{0}' at rank of {1}. You must add it first".format(getattr(self,modelFieldName), rankString)
                )

    def clean(self):
        if self.taxonRank == "species":
            self.validate_implied_taxon('order',order=self.order)
            self.validate_implied_taxon('family', family=self.family)
            self.validate_implied_taxon('subfamily', subfamily=self.subfamily)
            self.validate_implied_taxon('tribe', tribe=self.tribe)
            self.validate_implied_taxon('genus', genus=self.genus)
        if self.taxonRank == "genus":
            self.validate_implied_taxon('order', order=self.order)
            self.validate_implied_taxon('family', family=self.family)
            self.validate_implied_taxon('subfamily', subfamily=self.subfamily)
            self.validate_implied_taxon('tribe', tribe=self.tribe)
        if self.taxonRank == "tribe":
            self.validate_implied_taxon('order', order=self.order)
            self.validate_implied_taxon('family', family=self.family)
            self.validate_implied_taxon('subfamily', subfamily=self.subfamily)
        if self.taxonRank == "subfamily":
            self.validate_implied_taxon('order', order=self.order)
            self.validate_implied_taxon('family', family=self.family)
        if self.taxonRank == "family":
            self.validate_implied_taxon('order', order=self.order)

    def validate_unique(self, exclude=None):
        try:
            match = taxonomy.objects.filter(
                kingdom = self.kingdom,
                phylum = self.phylum,
                tclass = self.tclass,
                order = self.order,
                family = self.family,
                tribe = self.tribe,
                genus = self.genus,
                species = self.species,
                infraspecificEpithet = self.infraspecificEpithet,
                identificationQualifier=self.identificationQualifier,
                taxonRank=self.taxonRank
            )
            if len(match) > 0:
                raise ValidationError({NON_FIELD_ERRORS:'Matching taxon already exists'})
        except ObjectDoesNotExist:
            super(taxonomy, self).validate_unique()





class censusLocation(models.Model):
    fullName = models.CharField(max_length=100)
    shortName = models.CharField(max_length=20, unique=True)
    country = models.CharField(max_length=100, choices=CHOICES_Asian_country)
    mmAveragePrecipitation = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    minAltitude = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    maxAltitude = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    latitude = models.DecimalField(max_digits=25, decimal_places=10, null=True, blank=True)
    longitude = models.DecimalField(max_digits=25, decimal_places=10, null=True, blank=True)
    georefMethod = models.CharField(max_length=100, choices=CHOICES_georefMethod)
    datum = models.CharField(max_length=100, default="WGS84")
    WDPAID = models.IntegerField("ID from the World Database on Protected Areas", max_length=25, null=True, blank=True)

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
    presenceAbsenceOnly = models.BooleanField(default=False, verbose_name="Present")
    abundance = models.IntegerField(max_length=100, null=True, blank=True)
    issue = models.NullBooleanField(default=False)
    notes = models.CharField(max_length=200, null=True, blank=True, )

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

class functional_traits(models.Model):
    taxon = models.ForeignKey(taxonomy, null=False, blank=False, unique=True)
    browse_graze = models.CharField(max_length=100, null=True, blank=True, choices=CHOICES_BROWSEGRAZE)
    habitat = models.CharField(max_length=100, null=True, blank=True, choices=CHOICES_HABITAT)
    bodysize_brain_bunn = models.CharField(max_length=100, null=True, blank=True, choices=CHOICES_SIZE_BRAIN_BUNN)
    bodysize_lintulaakso = models.CharField(max_length=100, null=True, blank=True, choices=CHOICES_SIZE_LINTULAAKSO)
    bodysize_species_mean_kg = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    locomotor_reed = models.CharField(max_length=100, null=True, blank=True, choices=CHOICES_LOCOMOTOR_REED)
    trophic_lintulaakso = models.CharField(max_length=100, null=True, blank=True, choices=CHOICES_TROPHIC_LINTULAAKSO)

    def __unicode__(self):
        return 'Traits of ' + self.taxon.__unicode__()
    class Meta:
        db_table = 'functional_traits'
        verbose_name = "functional trait"
        verbose_name_plural = "functional traits"

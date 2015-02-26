from census_paleo.models import *
from django.contrib import admin
from django.contrib.auth.models import User,Group



#this is straight out of django docs

class taxonomyAdmin(admin.ModelAdmin):
    list_display = ("tclass","order","family","subFamily","tribe","genusName","specificEpithet")
    list_filter = ['tribe','taxonRank']

class censusLocationAdmin(admin.ModelAdmin):
    list_display = ("fullName","shortName","country","latitude","longitude")

class occurrenceAdmin(admin.ModelAdmin):
    list_filter = ["ref","location"]
    list_display = ["ref","location","taxon","abundance","presenceAbsenceOnly"]
    list_editable = ["abundance","presenceAbsenceOnly"]

admin.site.register(reference)
admin.site.register(taxonomy,taxonomyAdmin)
admin.site.register(censusLocation,censusLocationAdmin)
admin.site.register(occurrence, occurrenceAdmin)
admin.site.register(User)
admin.site.register(Group)
admin.site.register(fossilLocation)

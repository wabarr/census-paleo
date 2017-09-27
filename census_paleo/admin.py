from census_paleo.models import *
from django.contrib import admin
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin, AjaxSelectAdminTabularInline

#this is straight out of django docs

class OccurrenceInline(AjaxSelectAdminTabularInline):
    model = occurrence
    form = make_ajax_form(occurrence, {"ref": "referenceLookup", "taxon":"taxonLookup", "location":"locationLookup"})

class occurrenceAdmin(AjaxSelectAdmin):
    list_filter = ["ref","location"]
    list_display = ["ref","location","taxon","abundance","presenceAbsenceOnly"]
    list_editable = ["abundance","presenceAbsenceOnly"]
    search_fields = ["taxon__id", "taxon__species", "taxon__genus"]
    form = make_ajax_form(occurrence, {'ref': 'referenceLookup', 'location':'locationLookup', 'taxon':'taxonLookup'})

class taxonomyAdmin(admin.ModelAdmin):
    list_display = ['id','__unicode__','order','family','tribe','genus','species','ref','extant']
    list_filter = ['taxonRank','tribe', "family"]
    search_fields = ["id","genus", "species", "tribe", "subfamily", "family", "order"]
    list_editable = ['extant','ref']
    inlines = [OccurrenceInline, ]


class censusLocationAdmin(AjaxSelectAdmin):
    list_display = ('id',"fullName","shortName","country","latitude","longitude", "WDPAID")
    #inlines = [OccurrenceInline, ]
    search_fields = ["fullName", "shortName"]

class fossilLocationAdmin(AjaxSelectAdmin):
    list_display = ('id', "fullName", "projectArea","formation","member", "locality","submember")
    search_fields = ["fullName", "shortName"]

class referenceAdmin(admin.ModelAdmin):
    list_display = ["authorshortstring", "year","dataEntryComplete"]
    list_editable = ["year","dataEntryComplete"]
    #inlines = [OccurrenceInline,]

class functionalTraitAdmin(AjaxSelectAdmin):
    list_display = ['taxon','locomotor_reed','trophic_lintulaakso', 'trophic_rowan', 'locomotor_rowan']
    search_fields = ['taxon__id', 'taxon__genus', 'taxon__species']
    list_filter = ['browse_graze', 'locomotor_reed', 'trophic_lintulaakso', 'bodysize_lintulaakso']
    form = make_ajax_form(functional_traits, {"taxon":"taxonLookup"})

admin.site.register(reference, referenceAdmin)
admin.site.register(taxonomy,taxonomyAdmin)
admin.site.register(censusLocation,censusLocationAdmin)
admin.site.register(occurrence, occurrenceAdmin)
admin.site.register(fossilLocation, fossilLocationAdmin)
admin.site.register(functional_traits, functionalTraitAdmin)
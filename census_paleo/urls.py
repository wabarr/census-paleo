from django.conf.urls import patterns, include, url
from census_paleo.views import *
from ajax_select import urls as ajax_select_urls
#from tastypie.api import Api
from django.contrib import admin
#from census_paleo.api import OccurrenceResource, ReferenceResource, TaxonomyResource

# v1_api = Api(api_name='v1')
# v1_api.register(OccurrenceResource())
# v1_api.register(ReferenceResource())
# v1_api.register(TaxonomyResource())

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^occurrences/$',ViewOccurrences.as_view()),
    url(r'^occurrences/(?P<pk>[-\w]+)/$',ViewOccurrence.as_view(), name="occurrence_detail"),
    #url(r'^add_occurrences/$',enter_multiple_occurrences),
    url(r'^get_taxon_info_before_adding/$',get_taxon_info_before_adding),
    url(r'^add_taxon/$',add_taxon),
    url(r'^occurrence-pivot/$',occurrence_pivot),
    url(r'^occurrence-pivot-json/$',occurrence_pivot_json),
    url(r'^sites/$',sites),
    url(r'^sites/(?P<sitename>.+)/$',site_detail, name='site_detail'),
    url(r'^site_list/$',ViewSites.as_view(), name='site_list'),
    url(r'^sites_json/$',sites_json),
    url(r'^taxa/$',ViewTaxa.as_view(), name="taxon_list"),
    url(r'^taxa/(?P<pk>[-\w]+)/$', ViewTaxon.as_view(), name="taxon_detail"),
    #url(r'^occurrences-ajax/?',occurrences_ajax),
    url(r'^enter_occurrence/$', enter_occurrence, name="add_occurrence"),
    url(r'^enter_measured_value/$', enter_measured_value, name="add_measured_value"),
    url(r'^occurrence_table_json/$',occurrence_table_json),
    url(r'^resolve_taxon',resolve_taxon),
    url(r'^CSV_upload_occurrences_chooser',CSV_occurrence_upload_chooser, name='CSV_occurrence_upload_chooser'),
    url(r'^CSV_upload_functionalTrait_chooser',CSV_functionalTrait_upload_chooser, name='CSV_functionalTrait_upload_chooser'),
    #url(r'^CSV_upload_occurrences',CSV_occurrence_upload_formset, name='CSV_occurrence_upload_formset'),
    #url(r'^api/', include(v1_api.urls)),
    url(r'^$', enter_occurrence),
)

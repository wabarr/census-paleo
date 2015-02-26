from django.conf.urls import patterns, include, url
from census_paleo.views import *
from django.contrib.auth.decorators import login_required
from ajax_select import urls as ajax_select_urls
from tastypie.api import Api
#from census_paleo.api import OccurrenceResource, ReferenceResource, TaxonomyResource

# v1_api = Api(api_name='v1')
# v1_api.register(OccurrenceResource())
# v1_api.register(ReferenceResource())
# v1_api.register(TaxonomyResource())

# Uncomment the next two lines to enable the admin:
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),


    url(r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^occurrences/$',occurrences),
    url(r'^get_taxon_info_before_adding/$',get_taxon_info_before_adding),
    url(r'^add_taxon/$',add_taxon),
    url(r'^occurrence-pivot/$',occurrence_pivot),
    url(r'^occurrence-pivot-json/$',occurrence_pivot_json),
    url(r'^sites/$',sites),
    url(r'^sites/(?P<sitename>.+)/$',site_detail),
    url(r'^sites_json/$',sites_json),
    url(r'^taxa/$',login_required(view_taxa.as_view())),
    url(r'^occurrences-ajax/?',occurrences_ajax),
    url(r'^enter_occurrence/$', enter_occurrence),
    #url(r'^api/', include(v1_api.urls)),
    url(r'^$', census_home),
)

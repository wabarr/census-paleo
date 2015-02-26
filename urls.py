from django.conf.urls import patterns, include, url
from census_paleo import settings

import login.urls

urlpatterns = patterns('',

    # Uncomment the admin/doc line below to enable admin documentation:

    url(r'login', include(login.urls)),
    url(r'', include("census_paleo.urls"))


)

if settings.DEV:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Index page:
    (r'^$', 'thesite.views.index'),
    (r'^home/', 'thesite.views.index'),
    # FAQ
    (r'^info/', 'thesite.views.info'),
    # experiments
    (r'^experiments/', 'thesite.views.experiments'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

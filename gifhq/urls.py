from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# urls for the gifhq project
urlpatterns = patterns('',
    # url(r'^$', 'gifserver.views.home', name='home'),
    url(r'', include('gifserver.urls')),  # this is root, and everything else

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

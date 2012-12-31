from django.conf.urls import patterns, url

# urls for the gifserver app
urlpatterns = patterns('gifserver.views',
    url(r'^$', 'home', name='home'),
    url(r'^gifsite/(?P<gifsite_slug>\w+)/$', 'gifsite'),
    url(r'^gif/(?P<gif_id>\d+)/$', 'gif'),
)

from django.conf.urls import patterns, url

# urls for the gifserver app
urlpatterns = patterns('gifserver.views',
    url(r'^$', 'home', name='home'),
    url(r'^gifsites/$', 'gifsites', name="gifsites"),
    url(r'^gifsites/(?P<gifsite_slug>\w+)/$', 'gifsites', name="gifsites"),
    url(r'^gifs/$', 'gifs', name="gifs"),
    url(r'^gifs/(?P<gif_id>\d+)/$', 'gifs', name="gifs"),
)

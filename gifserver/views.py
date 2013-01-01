# Views, son.
from django.shortcuts import render_to_response, get_object_or_404
from gifserver.models import Gifsite, Gif


# home page
def home(request):
    gif_sites = Gifsite.objects.all().order_by('-date_added')[:5]
    gifs = Gif.objects.all().order_by('-date_added')[:10]

    return render_to_response(
        'gifserver/home.html', {
            'gifsites': gif_sites,
            'gifs': gifs,
            'page_title': 'home',
        }
    )


# a specific gifsite
def gifsites(request, gifsite_slug=False):
    if gifsite_slug:
        gif_site = get_object_or_404(Gifsite, slug=gifsite_slug)
        gifs = Gif.objects.filter(gifsite=gif_site.id).order_by('-date_added')[:10]
    else:
        gif_site = Gifsite.objects.all().order_by('-date_added')[:5],
        gifs = False

    return render_to_response(
        'gifserver/gifsites.html', {
            'gifsite': gif_site,
            'gifs': gifs,
            'page_title': 'gifsites',
        }
    )


# a specific gif
def gifs(request, gif_id=False):
    if gif_id:
        gif = get_object_or_404(Gif, pk=gif_id)
    else:
        gif = None
    return render_to_response(
        'gifserver/gifs.html', {
        'gif': gif,
        'page_title': 'gifs',
        }
    )

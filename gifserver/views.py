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
def gifsite(request, gifsite_slug=False):
    if gifsite_slug:
        gif_site = get_object_or_404(Gifsite, slug=gifsite_slug)
        gifs = Gif.objects.filter(gifsite=gif_site.id).order_by('-date_added')[:10]
    else:
        gif_site = Gifsite.objects.all().order_by('-date_added')[:5],
        gifs = False

    return render_to_response(
        'gifserver/gifsite.html', {
            'gifsite': gif_site,
            'gifs': gifs,
            'page_title': 'gifsite',
        }
    )


# a specific gif
def gif(request, gif_id):
    gif = get_object_or_404(Gif, pk=gif_id)
    return render_to_response(
        'gifserver/gif.html', {
        'gif': gif,
        'page_title': 'gif',
        }
    )

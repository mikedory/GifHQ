# Create your views here.
from django.shortcuts import render_to_response
from gifserver.models import Gifsite, Gif


def home(request):
    gif_sites = Gifsite.objects.all().order_by('-date_added')[:5]
    gifs = Gif.objects.all().order_by('-date_added')[:5]
    return render_to_response(
        'gifserver/home.html',
        {
            'gifsites': gif_sites,
            'gifs': gifs
        }
    )

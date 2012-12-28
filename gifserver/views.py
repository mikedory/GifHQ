# Create your views here.
from django.shortcuts import render_to_response
from gifserver.models import Gifsite


def home(request):
    gif_list = Gifsite.objects.all().order_by('-date_aded')[:5]
    return render_to_response(
        'gifserver/home.html',
        {
            'gif_list': gif_list
        }
    )

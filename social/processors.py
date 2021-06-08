from .models import Link


def contex_dictionary(request):
    links_contex = {}
    for link in Link.objects.all():
        links_contex[link.key] = link.url
    return links_contex

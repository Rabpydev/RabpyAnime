from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404

from App.models import Character

# Create your views here.

# def anime(request):
#     return HttpResponse("<h1>Anime</h1>")

def index(request):
    page = "home"
    return render(request, "index.html", {"page": page})

def anime(request):
    page = "anime"
    return render(request, "anime.html", {"page": page})

def contact(request):
    page = "contact"
    return render(request, "contact.html", {"page": page})

def characterall(request):
    page = "character"
    all_character = Character.objects.all()
    return render(request, "characterall.html", {"page": page, "all_character": all_character})


def character(request, character_id):
    character = Character.objects.get(pk=character_id)
    if character is not None:
        return render(request, 'character.html', {'character': character})
    else:
        raise Http404('Character does not exist')

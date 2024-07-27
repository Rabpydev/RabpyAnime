from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404

from App.models import Character
from App.models import Anime

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

# Create your views here.

# def anime(request):
#     return HttpResponse("<h1>Anime</h1>")

def index(request):
    page = "home" #กำหนด page เพื่อใช้ในการกำหนดเงื่อนไขการ Active เมนูใน Navbar (เงื่อนไขอยู่ที่ base.html)
    return render(request, "index.html", {"page": page})

# def anime(request):
#     page = "anime"
#     return render(request, "anime.html", {"page": page})

def animeall(request):
    page = "anime"
    all_anime = Anime.objects.all()
    return render(request, "anime_list.html", {"page": page, "all_anime": all_anime})

def anime(request, anime_id):
    anime = Anime.objects.get(pk=anime_id)
    if anime is not None:
        return render(request, 'anime.html', {'anime': anime})
    else:
        raise Http404('Anime does not exist')

def characterall(request):
    page = "character"
    all_character = Character.objects.all()
    return render(request, "character_list.html", {"page": page, "all_character": all_character})

def character(request, character_id):
    character = Character.objects.get(pk=character_id)
    if character is not None:
        return render(request, 'character.html', {'character': character})
    else:
        raise Http404('Character does not exist')

def contact(request):
    page = "contact"
    return render(request, "contact.html", {"page": page})
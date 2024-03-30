from django.contrib import admin
from App.models import Character, Anime, Category, Genre, Studio, ResourceAnime, ResourceCharacter

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ['name', 'created', 'updated']

class AnimeAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ['name', 'created', 'updated']

class CharacterAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ['show_image', 'name', 'gender', 'age']

class GenreAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ['name', 'created', 'updated']
                    
class StudioAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ['name', 'created', 'updated']

class ResourceAnimeAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ['name', 'created', 'updated']

class ResourceCharacterAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ['name', 'created', 'updated']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Anime, AnimeAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Studio, StudioAdmin)
admin.site.register(ResourceAnime, ResourceAnimeAdmin)
admin.site.register(ResourceCharacter, ResourceCharacterAdmin)
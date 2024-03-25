from django.contrib import admin
from App.models import Character, Anime, Category

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

admin.site.register(Category, CategoryAdmin)
admin.site.register(Anime, AnimeAdmin)
admin.site.register(Character, CharacterAdmin)
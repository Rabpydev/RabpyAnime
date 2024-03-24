from django.contrib import admin
from App.models import Character

# Register your models here.

class CharacterAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Character, CharacterAdmin)
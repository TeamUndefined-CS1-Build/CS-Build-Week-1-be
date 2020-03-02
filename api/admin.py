from django.contrib import admin
from .models import Character


class CharacterAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'last_modified',)


admin.site.register(Character, CharacterAdmin)
